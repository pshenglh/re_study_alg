def equal_index(l, left, right):
    if (l[left] > left and l[right] > right) or (l[left] < left and l[right] <right):
        return -1
    center = (left+right) / 2
    if center == l[center]:
        return center
    elif center < l[center]:
        equal_index(l, left, center)
    else:
        equal_index(l, center, right)

def test():
    l1 = [-1, 0, 2, 4, 8]
    l2 = [-1, 0, 1, 2, 3, 4]
    l3 = [1, 2, 3, 4, 5]
    for l in (l1, l2, l3):
        print equal_index(l, 0, len(l)-1)

if __name__ == '__main__':
    test()


