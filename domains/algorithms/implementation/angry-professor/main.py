if __name__ == '__main__':
    test_cases = int(input())
    for t in range(test_cases):
        n, k = [int(x) for x in input().strip().split(' ')]
        arrivals = [int(x) for x in input().strip().split(' ')]
        on_time_arrivals = sum([x <= 0 for x in arrivals])
        print("NO" if on_time_arrivals >= k else "YES")
