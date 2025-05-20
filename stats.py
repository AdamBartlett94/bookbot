def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_char_count(text: str) -> dict[int]:
    char_count_dict = {}
    for char in list(text):
        char_mod = char.lower()
        if char_mod not in char_count_dict:
            char_count_dict[char_mod] = 1
        else:
            char_count_dict[char_mod] += 1
    return char_count_dict


def sort_char_count(dict: dict) -> list[dict[str, int]]:
    sorted_dict = []
    for key in dict:
        tmp_dict = {"char": key, "num": dict[key]}
        sorted_dict.append(tmp_dict)
    sorted_dict.sort(reverse=True, key=lambda x: x["num"])
    return sorted_dict
