def parse():
    n = int(input().strip())
    matrix = []
    for i in range(n):
        matrix.append([int(x) for x in input().strip().split(' ')])
    return matrix

def diagonal_difference(matrix):
    sum1 = 0
    sum2 = 0
    for i in range(len(matrix)):
        sum1 += matrix[i][i]
        sum2 += matrix[i][len(matrix) - 1 - i]
    return abs(sum1 - sum2)

if __name__ == '__main__':
    print(diagonal_difference(parse()))
