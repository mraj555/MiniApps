from win32com.client import Dispatch


def speak(text):
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(text)

speak("Welcome, Mr.AJ")

# Copy the File
# Open Run and run "shell:startup"
# Paste the File in Startup Folder
# Rename File name from ***.py to ***.pyw