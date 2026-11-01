def get_num_words(book_content : str) -> int:
    n_words = len(book_content.split())

    print(f"Found {n_words} total words")

    return n_words
