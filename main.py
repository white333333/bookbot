def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents

def main():
    text_result = get_book_text("books/frankenstein.txt")
    print(text_result)

main()

