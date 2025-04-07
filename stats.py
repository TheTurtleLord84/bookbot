def words_in_book(text):
    words = text.split()
    return len(words)

def characters_map(text):
    characters = {}
    char_list = list(text)
    for char in char_list:
        chr = char.lower()
        if chr not in characters:
            characters[chr] = 1
        else:
            characters[chr] += 1
    return characters

def sort_dict(dict):
    new_dict = {}
    sorted_items = sorted(dict.items(), reverse=True, key=lambda item: item[1])
    for value in sorted_items:
        new_dict[value[0]] = value[1]

    return new_dict