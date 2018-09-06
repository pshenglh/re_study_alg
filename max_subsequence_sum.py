# encoding: utf8

def max_subsequence1(sequence):
    N = len(sequence)

    max_sum = 0
    for i in range(0, N):
        for j in range(i, N):
            this_sum = 0
            for k in range(i, j+1):
                this_sum += sequence[k]

            if this_sum > max_sum:
                max_sum = this_sum

    return max_sum

def max_subsequence2(sequence):

    max_sum = 0
    N = len(sequence)
    for i in range(0, N):
        this_sum = 0
        for j in range(i, N):
            this_sum += sequence[j]

            if this_sum > max_sum:
                max_sum = this_sum

    return max_sum

def max_subsequence3(sequence, left, right):
    if left == right:
        if sequence[left] > 0:
            return sequence[left]
        else:
            return 0

    center = (left+right) / 2
    max_left_sum = max_subsequence3(sequence, left, center)
    max_right_sum = max_subsequence3(sequence, center+1, right)

    max_left_border_sum = 0
    left_border_sum = 0
    for i in range(center, left-1, -1):
        left_border_sum += sequence[i]
        if left_border_sum > max_left_border_sum:
            max_left_border_sum = left_border_sum

    max_right_border_sum = 0
    right_border_sum = 0
    for j in range(center+1, right+1):
        right_border_sum += sequence[j]
        if right_border_sum > max_right_border_sum:
            max_right_border_sum = right_border_sum

    return max(max_left_sum, max_right_sum, max_left_border_sum+max_right_border_sum)

def max_subsequence4(sequence):
    this_sum = 0
    max_sum = 0

    for i in sequence:
        this_sum += i
        if this_sum > max_sum:
            max_sum = this_sum
        elif this_sum < 0:
            max_sum = 0

    return max_sum

def test():
    sequence = [1, 2, -3, 6, 9, -2, 100, -80]
    print max_subsequence1(sequence)
    print max_subsequence2(sequence)
    print max_subsequence3(sequence, 0, len(sequence)-1)
    print max_subsequence4(sequence)

if __name__ == '__main__':
    test()