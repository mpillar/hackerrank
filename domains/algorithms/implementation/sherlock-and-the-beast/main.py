def highest_decent_number_for(digits):
    for x in range(digits // 3, -1, -1):
        y = (digits - (3 * x)) // 5
        if 3 * x + 5 * y == digits:
            return '555' * x + '33333' * y
    return -1

if __name__ == '__main__':
    test_cases = int(input())
    for t in range(test_cases):
        print(highest_decent_number_for(int(input())))