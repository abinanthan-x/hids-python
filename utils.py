import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, config):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = config["email_sender"]
    msg["To"] = config["email_recipient"]

    try:
        server = smtplib.SMTP(config["smtp_server"], config["smtp_port"])
        server.starttls()
        server.login(config["email_sender"], config["email_password"])
        server.send_message(msg)
        server.quit()
        print("Email sent:", subject)
    except Exception as e:
        print("Failed to send email:", e)