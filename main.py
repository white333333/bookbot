from stats import count_words
from stats import count_characters
from stats import list_maker
from stats import sort_on
from stats import list_maker

def get_book_text(path):
    with open(path) as file:
        return file.read()

relative_path = "books/frankenstein.txt"

def main():
    return get_book_text(relative_path)

book_text = main()
counted_characters_final = count_characters(book_text)
    
print(f"Found {count_words(book_text)} total words")
#print(counted_characters_final)

dictionary_list = list_maker(counted_characters_final)
dictionary_list.sort(reverse=True, key=sort_on)

print(dictionary_list)
