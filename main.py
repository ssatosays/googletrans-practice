from googletrans import Translator


def main(source_text: str):
    tran = Translator()
    result_text: str = tran.translate(source_text, src="en", dest='ja').text
    print(result_text)


if __name__ == '__main__':
    source_text: str = "Hello, world."
    main(source_text)
