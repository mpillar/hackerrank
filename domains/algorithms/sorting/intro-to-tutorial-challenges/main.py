s = int(input())
_ = input()
a = list(sorted([int(x) for x in input().strip().split(' ')]))
print(a.index(s))
