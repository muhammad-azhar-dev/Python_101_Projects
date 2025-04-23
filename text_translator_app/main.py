from deep_translator import GoogleTranslator

def translate_lan(text, lang):
    Translated = GoogleTranslator(source="auto", target=lang)
    reesult = Translated.translate(text)
    print(reesult)

if __name__ == "__main__":
    translate_lan(input("Enter Text: "), input("Enter language: "))