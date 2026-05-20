# MiniProjects

A collection of lightweight Python utilities for everyday tasks.

## Tech Stack

| Component         | Technology              |
|-------------------|------------------------|
| Language          | Python 3.x             |
| HTTP Client       | requests               |
| Email             | smtplib (stdlib)       |
| Text-to-Speech    | pywin32 (Windows SAPI) |
| Wikipedia API     | wikipedia (pypi)       |
| News API          | newsapi.org           |
| Image Processing  | pywhatkit             |
| Translation       | googletrans           |
| Notifications     | plyer                 |
| Platform          | Windows                |

## Project Structure

```
MiniProjects/
├── README.md
├── LICENSE
├── requirements.txt
├── send_email.py            # Email sending utility
├── text_to_voice.py         # Text-to-speech utility
├── wiki_py.py               # Wikipedia search utility
├── news_repo.py             # News fetching utility
├── shut_sleep.py            # System control utility
├── say_name_on_startup.py   # Startup greeting utility
├── png_2_txt.py             # Image to ASCII art utility
├── trans_with_google.py     # Translation utility
├── self_destructive.py      # File deletion utility
└── notify.py                # Desktop notification utility
```

---

## Utilities

### 1. Email Sender (`send_email.py`)

Send emails via Gmail SMTP with TLS encryption.

**Architecture:**
```
┌────────────────────────────────────────────────────────┐
│                     send_email.py                      │
├────────────────────────────────────────────────────────┤
│                                                        │
│   ┌──────────────┐    ┌────────────────────────────┐   │
│   │ Credentials  │───▶│    smtplib.SMTP Client      │   │
│   │(email/pass)  │    │    smtp.gmail.com:587       │   │
│   └──────────────┘    │    TLS Encryption           │   │
│                       └─────────────┬──────────────┘   │
│                                   │                    │
│                                   ▼                    │
│                       ┌────────────────────────────┐   │
│                       │     Gmail SMTP Server       │   │
│                       └────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
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
┌────────────────────────────────────────────────────────┐
│                    text_to_voice.py                    │
├────────────────────────────────────────────────────────┤
│                                                        │
│   ┌──────────────┐    ┌────────────────────────────┐   │
│   │  Text Input  │───▶│  Dispatch("SAPI.SpVoice")  │   │
│   └──────────────┘    │  COM Object                │   │
│                       └─────────────┬──────────────┘   │
│                                   │                    │
│                                   ▼                    │
│                       ┌────────────────────────────┐   │
│                       │   Windows Audio Output     │   │
│                       │   (Speakers/Headphones)    │   │
│                       └────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

**Setup:**
```bash
pip install pywin32
```

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
┌────────────────────────────────────────────────────────┐
│                      wiki_py.py                        │
├────────────────────────────────────────────────────────┤
│                                                        │
│   ┌──────────────┐    ┌────────────────────────────┐   │
│   │ Topic Input  │───▶│  wikipedia.summary()       │   │
│   └──────────────┘    │  wikipedia.page()          │   │
│                       └─────────────┬──────────────┘   │
│                                   │                    │
│                                   ▼                    │
│                       ┌────────────────────────────┐   │
│                       │     Wikipedia API          │   │
│                       │     wikipedia.org          │   │
│                       └────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

**Setup:**
```bash
pip install wikipedia
```

**Usage:**
```bash
python wiki_py.py
```
Enter a topic when prompted to get a 2-sentence summary with a link to the full article.

---

### 4. News Fetcher (`news_repo.py`)

Fetch latest news articles using NewsAPI.

**Architecture:**
```
┌────────────────────────────────────────────────────────┐
│                      news_repo.py                      │
├────────────────────────────────────────────────────────┤
│                                                        │
│   ┌──────────────┐    ┌────────────────────────────┐   │
│   │   API Key    │───▶│  requests.get()             │   │
│   └──────────────┘    │  newsapi.org/v2/everything  │   │
│                       └─────────────┬──────────────┘   │
│                                   │                    │
│                                   ▼                    │
│                       ┌────────────────────────────┐   │
│                       │      NewsAPI Server         │   │
│                       │      newsapi.org            │   │
│                       └────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

**Setup:**
1. Get a free API key from [newsapi.org](https://newsapi.org)
2. Replace `YOUR_API_KEY` in `news_repo.py`

**Usage:**
```bash
python news_repo.py
```
Fetches top 10 Python-related news articles with a 5-second delay between each display.

---

### 5. System Control (`shut_sleep.py`)

Control system power state (shutdown or sleep).

**Architecture:**
```
┌────────────────────────────────────────────────────────┐
│                      shut_sleep.py                     │
├────────────────────────────────────────────────────────┤
│                                                        │
│   ┌──────────────┐    ┌────────────────────────────┐   │
│   │  os.system() │───▶│  shutdown /s /t 1          │   │
│   └──────────────┘    │  (Windows Shutdown)        │   │
│                       └────────────────────────────┘   │
│                                                        │
│   ┌──────────────┐    ┌────────────────────────────┐   │
│   │  os.system() │───▶│  rundll32 powrprof.dll     │   │
│   └──────────────┘    │  SetSuspendState (Sleep)    │   │
│                       └────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

**Usage:**
```bash
python shut_sleep.py
```

**Note:** Uncomment the desired function before running. Shutdown executes immediately with 1-second delay.

---

### 6. Startup Greeting (`say_name_on_startup.py`)

Speaks a greeting message when Windows starts.

**Architecture:**
```
┌────────────────────────────────────────────────────────┐
│                 say_name_on_startup.py                │
├────────────────────────────────────────────────────────┤
│                                                        │
│   ┌──────────────┐    ┌────────────────────────────┐   │
│   │  Greeting    │───▶│  Dispatch("SAPI.SpVoice") │   │
│   │  Text        │    │  COM Object                │   │
│   └──────────────┘    └─────────────┬──────────────┘   │
│                                   │                    │
│                                   ▼                    │
│                       ┌────────────────────────────┐   │
│                       │   Windows Audio Output     │   │
│                       │   (System Startup)         │   │
│                       └────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

**Setup:**
1. Copy the file to clipboard
2. Open Run (`Win + R`) and type `shell:startup`
3. Paste the file in the Startup folder
4. Rename the file from `*.py` to `*.pyw` (hides console window)

**Usage:**
```python
speak("Welcome, Mr.AJ")
```

---

### 7. Image to ASCII Art (`png_2_txt.py`)

Convert images to ASCII art using pywhatkit.

**Architecture:**
```
┌────────────────────────────────────────────────────────┐
│                      png_2_txt.py                      │
├────────────────────────────────────────────────────────┤
│                                                        │
│   ┌──────────────┐    ┌────────────────────────────┐   │
│   │ image.png    │───▶│  pywhatkit.image_to_ascii_art│ │
│   └──────────────┘    │  OCR + Character Mapping    │   │
│                       └─────────────┬──────────────┘   │
│                                   │                    │
│                                   ▼                    │
│                       ┌────────────────────────────┐   │
│                       │     Output: image.txt      │   │
│                       │     (ASCII Art)            │   │
│                       └────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

**Setup:**
```bash
pip install pywhatkit
```

**Usage:**
```python
import pywhatkit

pywhatkit.image_to_ascii_art("image.png", "image.txt")
```

**Input:** `image.png` (any image file)
**Output:** `image.txt` (ASCII art representation)

---

### 8. Translator (`trans_with_google.py`)

Translate text to any language using Google Translate.

**Architecture:**
```
┌────────────────────────────────────────────────────────┐
│                  trans_with_google.py                  │
├────────────────────────────────────────────────────────┤
│                                                        │
│   ┌──────────────┐    ┌────────────────────────────┐   │
│   │ Input Text   │───▶│  googletrans.Translator()   │   │
│   │ (English)    │    │  src="en", dest=<target>    │   │
│   └──────────────┘    └─────────────┬──────────────┘   │
│                                   │                    │
│                                   ▼                    │
│                       ┌────────────────────────────┐   │
│                       │     Google Translate API    │   │
│                       │     translate.google.com    │   │
│                       └────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

**Setup:**
```bash
pip install googletrans==4.0.0-rc1
```

**Usage:**
```bash
python trans_with_google.py
```

Follow the prompts to enter text and select target language. Supports 100+ languages.

---

### 9. Self-Destructive (`self_destructive.py`)

Delete the script file itself upon execution.

**Architecture:**
```
┌────────────────────────────────────────────────────────┐
│                  self_destructive.py                  │
├────────────────────────────────────────────────────────┤
│                                                        │
│   ┌──────────────┐    ┌────────────────────────────┐   │
│   │ sys.argv[0]  │───▶│  os.remove()              │   │
│   │ (self path)  │    │  Deletes the script file  │   │
│   └──────────────┘    └────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

**Usage:**
```bash
python self_destructive.py
```

**Warning:** This permanently deletes the script file. Use with caution.

---

### 10. Desktop Notification (`notify.py`)

Send desktop notifications using plyer.

**Architecture:**
```
┌────────────────────────────────────────────────────────┐
│                      notify.py                        │
├────────────────────────────────────────────────────────┤
│                                                        │
│   ┌──────────────┐    ┌────────────────────────────┐   │
│   │  Title/Msg   │───▶│  plyer.notification.notify│   │
│   └──────────────┘    │  System Notification API   │   │
│                       └─────────────┬──────────────┘   │
│                                   │                    │
│                                   ▼                    │
│                       ┌────────────────────────────┐   │
│                       │   Windows Notification      │   │
│                       │   Center                   │   │
│                       └────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

**Setup:**
```bash
pip install plyer
```

**Usage:**
```python
from plyer import notification

notification.notify(
    title="Python",
    message="I'm learning python programming language.",
    timeout=3
)
```

**Parameters:**
- `title`: Notification title
- `message`: Notification body text
- `timeout`: Duration in seconds (optional)

---

## Installation

```bash
pip install -r requirements.txt
```

## Dependencies

| Package          | Purpose                    | Source  |
|------------------|---------------------------|---------|
| requests         | HTTP client               | stdlib  |
| pywin32          | Windows COM interface     | pypi    |
| wikipedia        | Wikipedia API wrapper     | pypi    |
| pywhatkit        | Image to ASCII conversion | pypi    |
| googletrans      | Google Translate API     | pypi    |
| plyer            | Desktop notifications     | pypi    |
| smtplib          | Email sending            | stdlib  |
| time             | Sleep/delay functions     | stdlib  |
| os               | System commands          | stdlib  |
| sys              | Script path access       | stdlib  |

---

## Security Notes

- **Never commit real credentials** to version control
- Use Gmail App Passwords, not your main password
- Store API keys in environment variables
- Consider `.env` files with python-dotenv for sensitive data

---

## License

MIT License - See [LICENSE](LICENSE) file for details.