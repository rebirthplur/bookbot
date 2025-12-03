def count(text):
    total = len(text.split())
    return total


def get_char_count(text):
    string = text.lower()
    counts = {}
    for char in string :
        counts[char] = counts.get(char, 0) + 1
    return counts

def sort_char_count(char_counts):
    sort_count = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    return sort_count

def char_count_output(char_count):
    lines = []
    for key, value in char_count:
        if key.isalpha():
            lines.append(f"{key}: {value}")
    return "\n".join(lines)
