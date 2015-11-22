input()
array = [int(x) for x in input().strip().split(' ')]

num_positive = sum(x > 0 for x in array)
num_negative = sum(x < 0 for x in array)
num_zero = sum(x == 0 for x in array)

for num in [num_positive, num_negative, num_zero]:
    print("%.3f" % (num / float(len(array))))
