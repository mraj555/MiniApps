# Email Sender

A lightweight Python utility for sending emails via Gmail SMTP.

## Tech Stack

| Component     | Technology             |
|--------------|------------------------|
| Language      | Python 3.x             |
| Email Library | smtplib (stdlib)        |
| Protocol      | SMTP with TLS          |

## Architecture

```
┌─────────────────────────────────────────┐
│           send_email.py                 │
├─────────────────────────────────────────┤
│  User Config (email/password)           │
├─────────────────────────────────────────┤
│  send_email(to, subject, body)          │
│         │                              │
│         ▼                              │
│  ┌─────────────────┐                   │
│  │  SMTP Client    │                   │
│  │  smtp.gmail.com │                   │
│  │  Port 587 (TLS) │                   │
│  └────────┬────────┘                   │
│           │                             │
│           ▼                             │
│  ┌─────────────────┐                   │
│  │  Gmail Server   │                   │
│  └─────────────────┘                   │
└─────────────────────────────────────────┘
```

## Setup

1. **Install Python 3.x** (smtplib is included in stdlib)

2. **Configure credentials** in `send_email.py`:
   ```python
   email = "your_email@gmail.com"
   password = "your_16_char_app_password"
   ```

3. **Generate Gmail App Password**:
   - Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   - Create a new App Password for "Mail"
   - Use this 16-character password (no spaces)

## Usage

```python
from send_email import send_email

send_email("recipient@example.com", "Subject Here", "Email body text")
```

## Configuration

| Variable  | Description                          |
|-----------|--------------------------------------|
| `email`   | Sender Gmail address                 |
| `password`| 16-character Gmail App Password      |
| `to`      | Recipient email address              |
| `subject` | Email subject line                   |
| `body`    | Email message content                |

## Security Notes

- **Never commit real credentials** to version control
- Use Gmail App Passwords, not your main password
- Consider environment variables for production use