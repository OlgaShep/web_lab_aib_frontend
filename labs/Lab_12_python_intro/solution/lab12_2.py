import heapq as h
def medians_Oleg(n, sequence):
    sum_medians = 0
    min_heap = []
    max_heap = []

    for i in sequence:
        h.heappush(min_heap, -i)
        h.heappush(max_heap, -h.heappop(min_heap))
        if len(min_heap) < len(max_heap):
            h.heappush(min_heap, -h.heappop(max_heap))
        sum_medians += -min_heap[0]
    return sum_medians

if __name__ == '__main__':
    with open('input_2.txt', 'r') as file:
        n = int(file.readline())
        sequence = list(map(int, file.readline().split()))
        print(medians_Oleg(n, sequence))