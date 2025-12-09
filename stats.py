def count_words(text):
    splitted_text = text.split()
    return len(splitted_text)

def count_characters(text):
    character_dict = {}
    for i in text.lower():
        if i not in character_dict:
            character_dict[i] = 1
        elif i in character_dict:
            character_dict[i] += 1
    return character_dict

def list_maker(dict):
    dictionary_list = []
    for i in dict:
        dictionary_list.append({"char": i, "num":dict[i]})
    return dictionary_list

def sort_on(list):
    return list["num"]

