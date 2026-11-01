def main():
    contents = get_book_text("./books/frankenstein.txt")
    count_words(contents)

def get_book_text(path_to_file : str) -> str:
    file_contents = None
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def count_words(book_content : str) -> int:
    n_words = len(book_content.split())

    print(f"Found {n_words} total words")

    return n_words

main()
