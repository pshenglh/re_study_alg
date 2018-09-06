import math

def prime(n):
    if n == 1 or n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                return False
    return True

def test():
    for i in (1, 2, 3, 4, 6, 8, 9, 13, 17, 18, 21, 100001):
        print i, prime(i)

if __name__ == '__main__':
    test()