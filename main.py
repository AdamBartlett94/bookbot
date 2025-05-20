import os
import sys
from stats import get_num_words, get_char_count, sort_char_count


def main(args):
    # Extract book text:
    book_path = args[1]
    book_text = get_book_text(book_path)
    
    # Extract statistics:
    book_word_count = get_num_words(book_text)
    book_char_count = get_char_count(book_text)
    sorted_char_count = sort_char_count(book_char_count)

    # Display statistics:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_char_count:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


def get_book_text(path: str) -> str:
    with open(os.path.join(os.path.abspath(""), path)) as f:
        contents = f.read()
    return contents


if __name__ == "__main__":
    # Parse input arguments:
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(args)
