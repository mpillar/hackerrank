if __name__ == '__main__':
    _ = input()
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])
