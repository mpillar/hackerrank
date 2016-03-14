if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        px, py, qx, qy = [int(x) for x in input().split(' ')]
        sx = 2 * qx - px
        sy = 2 * qy - py
        print("%s %s" % (sx, sy))
