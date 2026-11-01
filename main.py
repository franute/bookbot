from stats import chars_dict_to_sorted_list, get_character_stats, get_num_words

def main():
    contents = get_book_text("./books/frankenstein.txt")
    get_num_words(contents)
    chars_stats = get_character_stats(contents)
    sorted_list = chars_dict_to_sorted_list(chars_stats)
    print(sorted_list)

def get_book_text(path_to_file : str) -> str:
    file_contents = None
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents



main()
