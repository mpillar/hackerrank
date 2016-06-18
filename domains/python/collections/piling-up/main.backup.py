t = int(input())


def find_next_largest_or_equal_value_after_n(n, array):
    result = None
    for a in array:
        if a >= n:
            if result is None:
                result = a
            else:
                result = min(a, result)
    return result


def replace_once_in_array(before, after, array):
    for i in range(len(array)):
        if array[i] == before:
            array[i] = after
            break
    return array


def is_stackable(side_lengths):
    previous_number_of_cubes = len(side_lengths)

    while len(side_lengths) > 3: # If we've reached 3, we've won. It's stackable.
        def can_stack(side_length, potential_new_side_lengths):
            return find_next_largest_or_equal_value_after_n(side_length, potential_new_side_lengths) is not None

        def do_stacking(side_length, potential_new_side_lengths):
            next_largest_or_equal = find_next_largest_or_equal_value_after_n(side_length, potential_new_side_lengths)
            return replace_once_in_array(next_largest_or_equal, a, potential_new_side_lengths)

        a = side_lengths[0]
        b = side_lengths[-1]

        print('---')
        print(side_lengths)

        # Try the smaller element first.
        if a < b:
            if can_stack(a, side_lengths[1:]):
                side_lengths = do_stacking(a, side_lengths[1:])
                print('>>> 1')
                print(side_lengths)
            if can_stack(b, side_lengths[0:-1]):
                print('>>> 2')
                print(side_lengths)
                side_lengths = do_stacking(b, side_lengths[1:])
        else:
            if can_stack(b, side_lengths[0:-1]):
                print("$$$ 1")
                print(side_lengths)
                side_lengths = do_stacking(b, side_lengths[1:])
            if can_stack(a, side_lengths[1:]):
                print("$$$ 2")
                print(side_lengths)
                side_lengths = do_stacking(a, side_lengths[1:])

        if previous_number_of_cubes == len(side_lengths):
            break

    return len(side_lengths) <= 3

def main():
    for i in range(t):
        print('--------------------')
        _ = input() # Ignore length.
        side_lengths = [int(x) for x in input().strip().split(' ')]
        print(side_lengths)
        if is_stackable(side_lengths):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
