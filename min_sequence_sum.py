def min_subsequence_sum(l):
    this_sum = 0
    min_sum = 0
    for i in l:
        this_sum += i
        if this_sum < min_sum:
            min_sum = this_sum
        elif this_sum > 0:
            this_sum = 0

    return min_sum


def test():
    sequence = [1, 2, -3, 6, 9, -2, 100, -80]
    print min_subsequence_sum(sequence)

if __name__ == '__main__':
    test()
