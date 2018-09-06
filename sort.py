from random import randint
from copy import deepcopy


def insertion_sort(a):
    length = len(a)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break


def shell_sort(a):
    h = len(a) / 2
    while h > 1:
        for j in range(h, len(a)):
            k = j
            while k >= h:
                if a[k] < a[k-h]:
                    a[k], a[k-h] = a[k-h], a[k]
                else:
                    break
        h = h / 2


def select_sort(a):
    length = len(a)
    for i in range(length):
        for j in range(i+1, length-1):
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]


def merge_sort(a):
    def merge(a, l, m, h):
        i = l; j = m + 1
        tmp = deepcopy(a)

        for k in range(l, h+1):
            if i > m:
                a[k] = tmp[j]
                j += 1
            elif j > h:
                a[k] = tmp[i]
                i += 1
            elif tmp[i] < tmp[j]:
                a[k] = tmp[i]
                i += 1
            else:
                a[k] = tmp[j]
                j += 1

    def sort(a, l, h):
        if l <= h:
            return
        m = (l+h) / 2
        sort(a, l, m)
        sort(a, m+1, h)
        merge(a, l, m, h)
    h = len(a) - 1
    sort(a, 0, h)


def quick_sort(a):
    def median(a, l, r):
        center = (l+r) / 2
        if a[l] > a[center]:
            a[l], a[center] = a[center],a [l]
        elif a[center] > a[r]:
            a[r], a[center] = a[center], a[r]
        elif a[l] > a[r]:
            a[l], a[r] = a[r], a[l]
        a[center], a[r-1] = a[r-1], a[center]
        return a[r-1]

    def sort(a, l, r):
        if l + 3 <= r:
            pivot = median(a, l, r)
            i = l; j = r
            while True:
                while a[i] < pivot:
                    i += 1
                while a[j] > pivot:
                    j -= 1
                if i < j:
                    a[i], a[j] = a[j], a[i]
                else:
                    break
            a[i], a[r-1] = a[r-1], a[i]
            sort(a, l, i-1)
            sort(a, i+1, r)
        else:
            insertion_sort(a)
    sort(a, 0, len(a)-1)


def test():
    l = []
    for i in range(30):
        l.append(randint(-20, 100))
    print 'origin list: ', l
    insertion_sort(l)
    print 'insert_sorted list: ', l
    select_sort(l)
    print 'select_sorted list: ', l
    shell_sort(l)
    print 'shell_sorted list: ', l
    merge_sort(l)
    print 'merge_sorted list: ', l
    quick_sort(l)
    print 'quick_sort list: ', l


if __name__ == '__main__':
    test()
