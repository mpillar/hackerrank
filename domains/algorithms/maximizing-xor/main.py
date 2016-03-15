def max_xor(l, r):
    """
    Find the maximum value for a ^ b such that l <= a <= b <= r.
    """
    result = l ^ r
    for a in range(l, r+1):
        for b in range(a, r+1):
            result = max(result, a ^ b)
    return result

if __name__ == '__main__':
  print(max_xor(int(input()), int(input())))