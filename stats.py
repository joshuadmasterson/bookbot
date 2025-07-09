def get_word_count(filepath):
    wc = 0
    with open(filepath) as f:
        book_text = f.read()
        wc = len(book_text.split())
    return wc

def get_char_count(filepath):
    char_dict = {}
    with open(filepath) as f:
        book_text = f.read()
        for char in book_text:
            char = char.lower()
            if(char in char_dict):
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_dict(unsorted):
    def sort_on(stuff):
        return stuff["num"]

    sorted_list = []

    for key, value in unsorted.items():
        sorted_list.append({
            "name": key,
            "num": value
        })

    sorted_list.sort(reverse=True, key=sort_on)
    return list(sorted_list)