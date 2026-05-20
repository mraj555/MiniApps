import smtplib

email = "YOUR_EMAIL_ID"
# Go to https://myaccount.google.com/apppasswords and Generate Password and Enter it.
password = "YOUR_PASSWORD"  # 16-char App Password, no spaces


def send_email(to, subject, body):
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        s.login(email, password)
        s.sendmail(email, to, message)


send_email("RECEIVER_EMAIL_ID", "Hello!", "Hello, How are you?")
