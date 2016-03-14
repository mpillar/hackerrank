import string


def is_pangram(s):
    s = s.lower()
    for c in string.ascii_lowercase:
        if c not in s:
            return False
    return True


if __name__ == '__main__':
    print('pangram' if is_pangram(input().strip()) else 'not pangram')

