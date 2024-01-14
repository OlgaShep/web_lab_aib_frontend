def medians_Oleg(n, sequence):
    medians = []

    for i in range(n):
        sequence[:i + 1] = sorted(sequence[:i + 1])
        if (i + 1) % 2 == 1:
            median = sequence[(i + 1) // 2]
        else:
            median = sequence[i // 2]
        medians.append(median)

    return sum(medians)

if __name__ == '__main__':
    with open('input_2.txt', 'r') as file:
        n = int(file.readline())
        sequence = list(map(int, file.readline().split()))
        print(medians_Oleg(n, sequence))