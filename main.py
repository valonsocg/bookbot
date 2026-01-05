import sys

from stats import get_num_words, char_count, sort_dictionaries

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    char_counted = char_count(book_text)
    sorted_dictionaries = sort_dictionaries(char_counted)
    
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_dictionaries:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['num']}")
    print("============= END ===============")
    

main()
