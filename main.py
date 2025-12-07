def get_book_text(path):
    with open(path) as file:
        return file.read()

""" def main():
    text_result = get_book_text("books/frankenstein.txt")
    print(text_result) """

def main():
    print(get_book_text("books/frankenstein.txt"))

main()

