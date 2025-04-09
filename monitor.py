import re
import time
import json
import os

CONFIG_FILE = "config.json"
RULES_FILE = "rules.json"

def load_config():
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def load_rules():
    with open(RULES_FILE, 'r') as f:
        return json.load(f).get("rules", [])

def parse_execve_line(line):
    # Extracts arguments like a0=..., a1=... (handles quotes too)
    matches = re.findall(r'a\d+=(?:"([^"])"|\'([^\'])\'|([^ ]+))', line)
    args = [item for group in matches for item in group if item]
    return ' '.join(args) if args else None

def matches_rule(command, rule):
    return rule['pattern'] in command

def tail_log(log_file, last_position):
    with open(log_file, 'r') as f:
        f.seek(last_position)
        lines = f.readlines()
        new_position = f.tell()
    return lines, new_position

def monitor_audit_log(config, rules):
    log_file = config["audit_log_file"]
    last_position = os.path.getsize(log_file)

    print("[INFO] Monitoring started. Waiting for suspicious commands...")

    while True:
        time.sleep(2)
        try:
            lines, last_position = tail_log(log_file, last_position)
            for line in lines:
                if "type=EXECVE" in line:
                    command = parse_execve_line(line)
                    if command:
                        for rule in rules:
                            if matches_rule(command, rule):
                                print(f"[ALERT] Rule matched: {rule['name']} | Command: {command}")
        except Exception as e:
            print(f"[ERROR] {e}")

if __name__ == "__main__":
    config = load_config()
    rules = load_rules()
    monitor_audit_log(config, rules)
