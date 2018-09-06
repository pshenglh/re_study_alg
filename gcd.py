def gcd(m, n):
    while n > 0:
        rem = m % n
        m = n
        n = rem

    return m


def test():
    print gcd(9, 15)
    print gcd(49, 56)


if __name__ == '__main__':
    test()
