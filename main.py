def get_book_text(path):
    with open(path) as file:
        return file.read()

relative_path = "books/frankenstein.txt"

def main():
    return get_book_text(relative_path)

book_text = main()

def count_words(text):
    splitted_text = text.split()
    return len(splitted_text)
    
print(f"Found {count_words(book_text)} total words")
