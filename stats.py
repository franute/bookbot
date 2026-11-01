def get_num_words(book_content : str) -> int:
    n_words = len(book_content.split())

    print(f"Found {n_words} total words")

    return n_words

def sort_on(character: tuple[str, int]) -> int:
    return character[1]

def chars_dict_to_sorted_list(char_stats: dict[str, int]) -> list[tuple[str, int]]:
    sorted_list = []

    for key, value in char_stats.items():
        sorted_list.append((key, value))

    sorted_list = sorted(sorted_list, reverse=True, key=sort_on)

    return sorted_list

def get_character_stats(book_content : str) -> dict[str, int]:
    stats = {}

    for character in book_content:
        lower_character = character.lower()

        if not lower_character in stats:
            stats[lower_character] = 0

        stats[lower_character] = stats[lower_character] + 1

    return stats
