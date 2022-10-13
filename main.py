from googletrans import Translator


def translate_text(text='Turtle', src='en', dest='be'):
    try:
        translator = Translator()
        translation = translator.translate(text=text, src=src, dest=dest)

        return translation.text
    except Exception as ex:
        return f'{ex=}'


def main():
    print(translate_text())


if __name__ == '__main__':
    main()
