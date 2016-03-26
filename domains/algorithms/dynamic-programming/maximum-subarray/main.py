def sum_of_max_non_continuous_subarray(array):
    positives = [a for a in array if a > 0]
    if len(positives) > 0:
        return sum(positives)
    return max(array)


def sum_of_max_continuous_subarray(array):
    best_max = array[0]
    current_max = array[0]
    for i in range(1, len(array)):
        current_max = max(array[i], current_max + array[i])
        best_max = max(best_max, current_max)
    return best_max


if __name__ == '__main__':
    t = int(input())
    for t in range(t):
        n = int(input())
        a = [int(i) for i in input().strip().split(' ')]
        print("%s %s" % (sum_of_max_continuous_subarray(a), sum_of_max_non_continuous_subarray(a)))
