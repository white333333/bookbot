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

def sort_on(item):
    return item["num"]

def list_maker(item):
    dictionary_list = []
    for i in item:
        if i.isalpha()==True:
            dictionary_list.append({"char": i, "num":item[i]})
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list



