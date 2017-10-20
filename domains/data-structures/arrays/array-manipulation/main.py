def evaluate_ops(n, ops):
    array = [0] * (n+1)
    for op in ops:
        a, b, k = op
        array[a-1] += k
        array[b] -= k
    result = 0
    current = 0
    for i in range(n):
        current += array[i]
        result = max(result, current)
    return result


def parse():
    n, m = [int(x) for x in input().strip().split(' ')]
    ops = []
    for i in range(m):
        a, b, k = [int(x) for x in input().strip().split(' ')]
        ops.append((a, b, k))
    return n, ops


if __name__ == '__main__':
    print(evaluate_ops(*parse()))
