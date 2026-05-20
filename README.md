# MiniProjects

A collection of lightweight Python utilities for everyday tasks.

## Tech Stack

| Component       | Technology              |
|----------------|------------------------|
| Language       | Python 3.x             |
| Email          | smtplib (stdlib)       |
| Text-to-Speech | pywin32 (SAPI)         |
| Platform       | Windows                |

## Utilities

### 1. Email Sender (`send_email.py`)

Send emails via Gmail SMTP with TLS encryption.

**Architecture:**
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

**Setup:**
1. Configure credentials in `send_email.py`:
   ```python
   email = "your_email@gmail.com"
   password = "your_16_char_app_password"
   ```
2. Generate Gmail App Password at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

**Usage:**
```python
from send_email import send_email

send_email("recipient@example.com", "Subject Here", "Email body text")
```

**Dependencies:** smtplib (stdlib)

---

### 2. Text-to-Voice (`text_to_voice.py`)

Convert text to speech using Windows SAPI (Speech API).

**Architecture:**
```
┌─────────────────────────────────────────┐
│         text_to_voice.py                │
├─────────────────────────────────────────┤
│  audiobook(text)                        │
│         │                              │
│         ▼                              │
│  ┌─────────────────┐                   │
│  │  Dispatch SAPI   │                   │
│  │  SpVoice Object  │                   │
│  └────────┬────────┘                   │
│           │                             │
│           ▼                             │
│  ┌─────────────────┐                   │
│  │  Windows Audio   │                   │
│  │  Output Device   │                   │
│  └─────────────────┘                   │
└─────────────────────────────────────────┘
```

**Setup:**
1. Install pywin32: `pip install pywin32`

**Usage:**
```python
from text_to_voice import audiobook

audiobook("This is a book text.")
```

**Dependencies:** pywin32

---

## Installation

```bash
pip install -r requirements.txt
```

## Project Structure

```
MiniProjects/
├── README.md
├── requirements.txt
├── send_email.py
└── text_to_voice.py
```

## Security Notes

- **Never commit real credentials** to version control
- Use Gmail App Passwords, not your main password
- Consider environment variables for sensitive data

## License

MIT License