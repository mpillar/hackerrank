def is_stackable(side_lengths):
    current_top_of_stack = max(side_lengths[0], side_lengths[-1])
    while len(side_lengths) > 1:
        # Choose the larger of both sides.
        if side_lengths[0] > side_lengths[-1]:
            next_top_of_stack = side_lengths[0]
            del side_lengths[0]
        else:
            next_top_of_stack = side_lengths[-1]
            del side_lengths[-1]
        if next_top_of_stack > current_top_of_stack:
            return False
        current_top_of_stack = next_top_of_stack
    return True


def main():
    t = int(input())
    for i in range(t):
        _ = input() # Ignore length.
        side_lengths = [int(x) for x in input().strip().split(' ')]
        print('Yes' if is_stackable(side_lengths) else 'No')


if __name__ == '__main__':
    main()
