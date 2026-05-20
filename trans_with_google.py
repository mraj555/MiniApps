from googletrans import Translator, LANGUAGES

lang = list(LANGUAGES.values())
print("Welcome to PyGuy Translate")

input_text = input("Please Enter Any Text In English: \n")
out_lang = input(
    "Please Enter Output Language Name (ex. - Hindi, Gujarati, etc.): \n"
).lower()

if out_lang not in lang:
    print("Sorry, This Language is not available to translate")
else:
    translator = Translator()
    result = translator.translate(text=input_text, src="en", dest=out_lang)
    print(f"Translated: {result.text}")
    print(f"Pronunciation: {result.pronunciation}")
