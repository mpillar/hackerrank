def lonelyinteger(b):
    import collections
    m = collections.defaultdict(int)
    for e in b:
        m[e] += 1
    for k in m.keys():
        if m[k] == 1:
            return k


if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
