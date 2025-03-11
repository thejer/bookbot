
def get_num_words(content):
    return len(content.split())

def count_chars(text):
    count = {}
    for char in text.lower():
        count[char] = count.get(char, 0) + 1
    return count

def sort_char_count(char_count):
    sorted_list = [{"char": char, "count": count} for char, count in char_count.items()]
    sorted_list.sort(reverse=False, key=lambda x: x['char'])
    return sorted_list