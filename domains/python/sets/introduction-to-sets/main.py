_ = input() # ignore first line
data = set([int(x) for x in input().strip().split(' ')])
print(sum(data)/len(data))
