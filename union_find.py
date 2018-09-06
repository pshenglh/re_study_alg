

class UF(object):

    def __init__(self, n):
        self.s = [-1] * n

    def union(self, x, y):
        if self.size(self.find(x)) <= self.size(self.find(y)):
            self.s[self.find(x)] = self.size(self.find(x)) + self.size(self.find(y))
            self.s[y] = x
        else:
            self.s[self.find(y)] = self.size(self.find(x)) + self.size(self.find(y))
            self.s[x] = self.s[y]

    def find(self, x):
        if self.s[x] < 0:
            return x
        else:
            self.s[x] = self.find(self.s[x])
            return self.s[x]

    def size(self, root):
        if self.s[root] > 0:
            return 'error size'
        else:
            return self.s[root]


def test():
    n = 10
    uf = UF(n)
    uf.union(3, 5)
    print uf.find(5)
    uf.union(5, 2)
    print uf.find(2)
    uf.union(2, 7)
    print uf.find(7)
    uf.union(8, 1)
    print uf.find(1)


if __name__ == '__main__':
    test()
