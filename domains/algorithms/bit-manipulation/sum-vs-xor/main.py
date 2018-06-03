def solve(n):
    """
    Given n, find each x such that:
       0 <= x <= n
       n + x = n ^ x
    Output the total number of integers x satisfying the criteria.
    
    Approach:
    Per https://www.geeksforgeeks.org/equal-sum-xor/, we count the unset
    bits in n and the result is 2 ** (count of unset bits in n).
    """
    
    unset_bits = 0
    while n > 0:
        last_bit = n & 0x1
        if last_bit == 0:
            unset_bits += 1
        n >>= 1
    
    return 2 ** unset_bits

if __name__ == '__main__':
    assert(2 == solve(5))
