def main():
    contents = get_book_text("./books/frankenstein.txt")
    print(contents)

def get_book_text(path_to_file : str) -> str:
    file_contents = None
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

main()
