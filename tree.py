class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        if self.value == 0:
            self.height = 0
        else:
            self.height = 1

    def __repr__(self):
        return 'Node {}'.format(self.value)


class SearchTree(object):

    def __init__(self):
        self.root = Node(None)

    def find(self, v):
        n = self.root
        return self.__find(v, n)

    def __find(self, v, n):
        if not n.value:
            return None
        if n.value < v:
            return self.__find(v, n.left)
        elif n.value > v:
            return self.__find(v, n.right)
        else:
            return n

    def find_min(self):
        n = self.root
        return self.__find_min(n)

    def __find_min(self, n):
        if not n.value:
            return None
        elif not n.left:
            return n
        else:
            return self.__find_min(n.left)

    def find_max(self):
        n = self.root
        return self.__find_max(n)

    def __find_max(self, n):
        if not n.value:
            return None
        elif not n.right:
            return n
        else:
            return self.__find_max(n.right)

    def insert(self, v):
        n = self.root
        self.root = self.__insert(v, n)

    def __insert(self, v, n):
        if n == self.root and not n.value:
            n.value = v
        if not n:
            return Node(v)
        elif v < n.value:
            n.left = self.__insert(v, n.left)
            return n
        elif v > n.value:
            n.right = self.__insert(v, n.right)
            return n
        else:
            return n

    def pre_traverse(self):
        n = self.root
        self.__pre_traverse(n)
        print '\n'

    def __pre_traverse(self, n):
        if not n:
            return
        else:
            print n.value,
            self.__pre_traverse(n.left)
            self.__pre_traverse(n.right)

    def middle_traverser(self):
        n = self.root
        self.__middle_traverse(n)

    def __middle_traverse(self, n):
        if not n:
            return
        else:
            self.__middle_traverse(n.left)
            print n.value,
            self.__middle_traverse(n.right)

    def delete(self, v):
        n = self.root
        self.__delete(v, n)

    def __delete(self, v, n):
        if not n:
            return
        elif v < n.value:
            n.left = self.__delete(v, n.left)
            return n
        elif v > n.value:
            n.right = self.__delete(v, n.right)
            return n
        else:
            if not n.left:
                n = n.right
                return n
            elif not n.right:
                n = n.left
                return n
            else:
                tmp_node = self.__find_min(n.right)
                n.value = tmp_node.value
                n.right = self.__delete(tmp_node.value, n.right)
                return n


def test():
    t = SearchTree()
    t.insert(5)
    t.insert(10)
    t.insert(3)
    t.insert(20)
    t.insert(7)
    t.insert(4)
    t.insert(15)
    t.insert(24)
    t.pre_traverse()
    print t.find_min()
    print t.find_max()
    t.delete(10)
    t.pre_traverse()
    t.middle_traverser()

if __name__ == '__main__':
    test()
