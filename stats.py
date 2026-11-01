def get_num_words(book_content : str) -> int:
    n_words = len(book_content.split())

    print(f"Found {n_words} total words")

    return n_words

def get_character_stats(book_content : str) -> dict[str, int]:
    stats = {}

    for character in book_content:
        lower_character = character.lower()

        if not lower_character in stats:
            stats[lower_character] = 0

        stats[lower_character] = stats[lower_character] + 1

    return stats
