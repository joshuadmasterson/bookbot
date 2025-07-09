import sys

from stats import get_word_count, get_char_count, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        print(f.read())

def main():
    # get_book_text()
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
     
    book_path = sys.argv[1]
    wc = get_word_count(book_path)
    char_dict = get_char_count(book_path)
    char_list = sort_dict(char_dict)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Analyzing book found at {book_path}...")
    print(f"Found {wc} total words")
    print(f"--------- Character Count -------")
    for item in char_list:
        if item["name"].isalpha():
            print(f"{item["name"]}: {item["num"]}")
    print(f"============= END ===============")

main()