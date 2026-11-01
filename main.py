import sys
from stats import chars_dict_to_sorted_list, get_character_stats, get_num_words

def main():
    book_path = None

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    contents = get_book_text(book_path)
    n_words = get_num_words(contents)
    chars_stats = get_character_stats(contents)
    sorted_list = chars_dict_to_sorted_list(chars_stats)
    print_report(book_path, n_words, sorted_list)

def get_book_text(path_to_file : str) -> str:
    file_contents = None
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def print_report(book_path: str, word_count: int, characters_stats: list[tuple[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character, count in characters_stats:
        if character.isalpha():
            print(f"{character}: {count}")

    print("============= END ===============")

main()
