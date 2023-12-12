with open('input.txt', 'r') as file:
    n = int(file.readline())
    sequence = list(map(int, file.readline().split()))
    medians = []

    for i in range(n):
        sequence[:i+1] = sorted(sequence[:i+1])
        if (i + 1) % 2 == 1:
            median = sequence[(i + 1) // 2]
        else:
            median = sequence[i // 2]
        medians.append(median)

    total_sum = sum(medians)
    print(total_sum)