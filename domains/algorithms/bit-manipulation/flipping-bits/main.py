def flip_bits(uint32):
    return uint32 ^ 0xffffffff

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print(flip_bits(int(input())))
