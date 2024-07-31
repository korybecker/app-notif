# send_notif.py
import sqlite3
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# load env vars
load_dotenv()

SMTP_SERVER = os.getenv('SMTP_SERVER_UPDATED')
SMTP_PORT = os.getenv('SMTP_PORT')
FROM_EMAIL_ADDRESS = os.getenv('FROM_EMAIL_ADDRESS_UPDATED')
FROM_EMAIL_PASSWORD = os.getenv('FROM_EMAIL_PASSWORD_UPDATED2')
TO_EMAIL_ADDRESS = os.getenv('TO_EMAIL_ADDRESS')

def send_email(to_address, subject, body):
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = FROM_EMAIL_ADDRESS
        msg['To'] = to_address

        part = MIMEText(body, 'html')
        msg.attach(part)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(FROM_EMAIL_ADDRESS, FROM_EMAIL_PASSWORD)
            server.sendmail(FROM_EMAIL_ADDRESS, to_address, msg.as_string())
        print("Notification email sent")
    except smtplib.SMTPException as e:
        print(f'Error sending email: {e}')
    except Exception as e:
        print(f"Unexpected error in send_email: {e}")

def check_apps():
    try:
        conn = sqlite3.connect('applications.db')
        c = conn.cursor()
        one_week_ago = datetime.now() - timedelta(days=7)
        one_week_ago_str = one_week_ago.strftime('%Y-%m-%d')

        c.execute('''
            SELECT company, position, date_applied, job_url
            FROM apps
            WHERE date_applied = ?
        ''', (one_week_ago_str,))

        apps = c.fetchall()
        conn.close()

        if apps:
            subject = "Follow-Up Reminder: Job Applications"
            body = "<h2>These applications are 1 week old:</h2><ul>"
            for app in apps:
                body += f"<li><b>Company:</b> {app[0]}<br><b>Position:</b> {app[1]}<br><b>Date Applied:</b> {app[2]}<br><b>Job URL:</b> <a href='{app[3]}'>{app[3]}</a></li><br>"
            body += "</ul>"
            
            send_email(TO_EMAIL_ADDRESS, subject, body)
            print("Notification email sent")
        else:
            print("No applications to follow up on today")
    except sqlite3.Error as e:
        print(f'SQLite error: {e}')
    except Exception as e:
        print(f'Unexpected error in check_apps: {e}')


if __name__ == "__main__":
    check_apps()
