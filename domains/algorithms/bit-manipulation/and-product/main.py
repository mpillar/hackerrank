def only_last_bit(x):
    for i in range(32):
        if x >> i & 0x00000001 > 0:
            return 1 << i


def and_of_range(a, b):
    result = 0xffffffff
    counter = min(a, b)
    while counter < max(a, b) + 1:
        result &= counter
        if result == 0: return result
        counter = result + only_last_bit(result)
    return result


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print(and_of_range(*[int(x) for x in input().strip().split(' ')]))

