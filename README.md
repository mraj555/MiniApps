# MiniProjects

A collection of lightweight Python utilities for everyday tasks.

## Tech Stack

| Component         | Technology              |
|-------------------|------------------------|
| Language          | Python 3.x             |
| Email             | smtplib (stdlib)       |
| Text-to-Speech    | pywin32 (Windows SAPI) |
| Wikipedia API     | wikipedia (pypi)       |
| Platform          | Windows                |

## Project Structure

```
MiniProjects/
├── README.md
├── requirements.txt
├── send_email.py       # Email sending utility
├── text_to_voice.py    # Text-to-speech utility
└── wiki_py.py          # Wikipedia search utility
```

## Utilities

### 1. Email Sender (`send_email.py`)

Send emails via Gmail SMTP with TLS encryption.

**Architecture:**
```
┌─────────────────────────────────────────────────────┐
│                    send_email.py                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│   ┌─────────────┐      ┌─────────────────────────┐ │
│   │ Credentials │─────▶│  smtplib.SMTP Client    │ │
│   │(email/pass) │      │  smtp.gmail.com:587     │ │
│   └─────────────┘      │  TLS Encryption          │ │
│                        └───────────┬─────────────┘ │
│                                    │               │
│                                    ▼               │
│                        ┌─────────────────────────┐ │
│                        │     Gmail SMTP Server    │ │
│                        └─────────────────────────┘ │
└─────────────────────────────────────────────────────┘
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

---

### 2. Text-to-Voice (`text_to_voice.py`)

Convert text to speech using Windows SAPI (Speech API).

**Architecture:**
```
┌─────────────────────────────────────────────────────┐
│                   text_to_voice.py                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│   ┌─────────────┐      ┌─────────────────────────┐ │
│   │ Text Input  │─────▶│  Dispatch("SAPI.SpVoice")│ │
│   └─────────────┘      │  COM Object              │ │
│                        └───────────┬─────────────┘ │
│                                    │               │
│                                    ▼               │
│                        ┌─────────────────────────┐ │
│                        │  Windows Audio Output   │ │
│                        │  (Speakers/Headphones)   │ │
│                        └─────────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

**Setup:**
1. Install pywin32: `pip install pywin32`

**Usage:**
```python
from text_to_voice import audiobook

audiobook("This is a book text.")
```

---

### 3. Wikipedia Search (`wiki_py.py`)

Search and retrieve summaries from Wikipedia.

**Architecture:**
```
┌─────────────────────────────────────────────────────┐
│                     wiki_py.py                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│   ┌─────────────┐      ┌─────────────────────────┐ │
│   │ Topic Input │─────▶│  wikipedia.summary()     │ │
│   └─────────────┘      │  wikipedia.page()        │ │
│                        └───────────┬─────────────┘ │
│                                    │               │
│                                    ▼               │
│                        ┌─────────────────────────┐ │
│                        │   Wikipedia API         │ │
│                        │   wikipedia.org         │ │
│                        └─────────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

**Setup:**
1. Install wikipedia: `pip install wikipedia`

**Usage:**
```bash
python wiki_py.py
```
Enter a topic when prompted to get a 2-sentence summary with a link to the full article.

---

## Installation

```bash
pip install -r requirements.txt
```

## Dependencies

| Package     | Purpose                    | Source  |
|-------------|---------------------------|---------|
| pywin32     | Windows COM interface     | pypi    |
| wikipedia   | Wikipedia API wrapper     | pypi    |
| smtplib     | Email sending (built-in)  | stdlib  |

## Security Notes

- **Never commit real credentials** to version control
- Use Gmail App Passwords, not your main password
- Consider environment variables for sensitive data

## License

MIT License