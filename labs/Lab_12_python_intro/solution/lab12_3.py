def break_pentagon(text):
    char_count = {}
    for char in text:
        if char not in {' ', '\n'}:
            char_count[char] = char_count.setdefault(char, 0) + 1

    sorted_chars = sorted(char_count.keys())
    max_count = max(char_count.values())

    for i in range(max_count, 0, -1):
        line = ''
        for char in sorted_chars:
            if char_count.get(char, 0) >= i:
                line += '#'
            else:
                line += ' '
        print(line)

    return ''.join(sorted_chars)

if __name__ == '__main__':
    with open('input_3.txt', 'r') as file:
        text = file.read()
        print(break_pentagon(text))