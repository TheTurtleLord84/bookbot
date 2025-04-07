from stats import characters_map, words_in_book, sort_dict
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_contents = f.read()
    return book_contents

def print_output(book_path, w, dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {w} total words")
    print("--------- Character Count -------")
    for key in dict:
        if key.isalpha():
            print(f"{key}: {dict[key]}")
    print("============= END ===============")


def main(): 
    try:
        book_path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    t = get_book_text(book_path)
    w = words_in_book(t)
    chars = characters_map(t)
    dict = sort_dict(chars)
    print_output(book_path, w, dict)
    

main()
