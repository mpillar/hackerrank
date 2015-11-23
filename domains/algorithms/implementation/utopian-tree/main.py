def height_after_cycles(cycles):
    if cycles == 0:
        return 1
    elif cycles % 2 == 0:
        return 1 + height_after_cycles(cycles - 1)
    else:
        return 2 * height_after_cycles(cycles - 1)

if __name__ == '__main__':
    test_cases = int(input())
    for t in range(test_cases):
        print(height_after_cycles(int(input())))