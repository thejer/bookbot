from stats import get_num_words, count_chars, sort_char_count
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content
    
def print_sorted_count(sorted_list):
    for item in sorted_list:
        print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    num_words = get_num_words(content)
    char_count = count_chars(content)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for item in sort_char_count(char_count):
        if item["char"].isalpha():
             print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

main()