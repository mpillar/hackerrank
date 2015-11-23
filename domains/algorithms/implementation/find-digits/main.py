def num_digits_that_divide_n(n):
    digits = [int(x) for x in list(str(n))]
    result = 0
    for d in digits:
        if d != 0 and n % d == 0:
            result += 1
    return result

if __name__ == '__main__':
    test_cases = int(input())
    for t in range(test_cases):
        print(num_digits_that_divide_n(int(input())))