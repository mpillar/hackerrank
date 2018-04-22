def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
            continue
        remainder = grade % 5
        if remainder <= 2:
            result.append(grade)
            continue
        result.append(int(grade / 5) * 5 + 5)
    return result


if __name__ == '__main__':
    test_cases = int(input())
    grades = []
    for t in range(test_cases):
        grades.append(int(input()))
    grades = gradingStudents(grades)
    print("\n".join(map(str, grades)))
