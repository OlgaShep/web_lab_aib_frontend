with open('input.txt', 'r') as file:
    text = file.read()
    char_count = {}
    for char in text:
        if char not in char_count and char != ' ' and char != '\n':
            char_count[char] = 1
        elif char != ' ' and char != '\n':
            char_count[char] += 1

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

    symbols_line = ''.join(sorted_chars)
    print(symbols_line)