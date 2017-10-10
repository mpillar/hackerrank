def compute_max_hourglass_sum(data):
    result = -9 * 7 # Lowest possible value
    for i in range(1, 5):
        for j in range(1, 5):
            hourglass_sum = data[i-1][j-1] + data[i-1][j] + data[i-1][j+1] + \
                                             data[i][j] + \
                            data[i+1][j-1] + data[i+1][j] + data[i+1][j+1]

            result = max(result, hourglass_sum)
    return result


def parse():
    data = []
    for i in range(6):
        data.append([int(x) for x in input().strip().split(' ')])
    return data


if __name__ == '__main__':
    print(compute_max_hourglass_sum(parse()))
