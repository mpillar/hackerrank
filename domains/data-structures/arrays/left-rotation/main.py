def left_shift(quantity, array):
    return array[quantity:] + array[0:quantity]


if __name__ == '__main__':
    nd = input().split()
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = left_shift(d, a)
    print(' '.join([str(r) for r in result]))
