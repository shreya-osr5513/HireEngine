import smtplib
from email.mime.text import MIMEText
import os

# Read from Render Environment Variables
EMAIL = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASS")


def send_email(to_email, subject, body):
    if not EMAIL or not PASSWORD:
        print("❌ Email credentials not set in environment variables")
        return

    try:
        print("Connecting to Gmail...")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(EMAIL, PASSWORD)
        print("✅ Logged in successfully")

        msg = MIMEText(body, "plain", "utf-8")
        msg["Subject"] = subject
        msg["From"] = EMAIL
        msg["To"] = to_email

        server.sendmail(EMAIL, to_email, msg.as_string())
        server.quit()

        print(f"📧 Email sent to {to_email}")

    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed. Check EMAIL_USER / EMAIL_PASS")

    except Exception as e:
        print("❌ Email failed:", str(e))
