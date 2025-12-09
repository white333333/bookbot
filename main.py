from stats import count_words, count_characters, list_maker

def get_book_text(path):
    with open(path) as file:
        return file.read()

relative_path = "books/frankenstein.txt"

def main():
    return get_book_text(relative_path)

book_text = main()
counted_characters_final = count_characters(book_text)
dictionary_list = list_maker(counted_characters_final)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {relative_path}")
print("----------- Word Count ----------")
print(f"Found {count_words(book_text)} total words")
print("--------- Character Count -------")
for item in dictionary_list:
    letter = item["char"]
    count = item["num"]
    print(f"{letter}: {count}")
