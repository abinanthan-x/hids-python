# Linux Command Monitor with auditd + Python

This tool monitors Linux command executions using auditd and applies rule-based detection logic to alert on suspicious behavior.

## Features
- Real-time monitoring of executed commands
- Rule-based detection system
- Email alerts

## Requirements
- Python 3.8+
- auditd installed and running
- SMTP details configured in config.json

## How to Run
1. Install auditd:
   ```bash
   sudo apt install auditd
   sudo systemctl start auditd