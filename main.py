def main():
    path_to_file = "./books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item["count"]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered not in chars:
            chars[lowered] = 1
        else:
            chars[lowered] += 1
    return chars

def sort_by(d):
    return d["count"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for key in chars_dict:
        sorted_list.append({ "char": key, "count": chars_dict[key]})
    sorted_list.sort(reverse=True, key=sort_by)
    return sorted_list

main()
