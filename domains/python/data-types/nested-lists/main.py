
def main():
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append((name, score))

    grades.sort(key=lambda element: (element[1], element[0]))

    first_grade = grades[0][1]
    index = 1
    while grades[index][1] == first_grade:
        index += 1

    result = [grades[index][0]]
    result_grade = grades[index][1]
    index += 1
    while index+1 <= len(grades) and grades[index][1] == result_grade:
        result.append(grades[index][0])
        index += 1

    print('\n'.join(result))


if __name__ == '__main__':
    main()
