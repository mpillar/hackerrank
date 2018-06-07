def divisible_sum_pairs(n, k, ar):
    """
    Print the number of (i,j) pairs where i<j and a_i + a_j is evenly divisible
    by k.
    """
    result = 0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i] + ar[j]) % k == 0:
                result += 1
    return result
