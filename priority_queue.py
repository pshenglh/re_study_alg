class TreeNode(object):

    def __init__(self, element, left=None, right=None, npl=0):
        self.element = element
        self.left = left
        self.right = right
        self.npl = npl

    def __repr__(self):
        return '<TreeNode %r>' % self.element


class PriorityQueue(object):

    def __init__(self):
        self.root = None
        pass

    def merge(self, other):
        n1 = self.root
        n2 = other.root

        self.root = PriorityQueue.merge(n1, n2)

    @staticmethod
    def merge(n1, n2):
        if not n1:
            return n2
        if not n2:
            return n1
        if n1.element < n2.element:
            return PriorityQueue.merge1(n1, n2)
        else:
            return PriorityQueue.merge1(n2, n1)

    @staticmethod
    def merge1(h1, h2):
        if not h1.left:
            h1.left = h2
        else:
            h1.right = PriorityQueue.merge(h1.right, h2)
            if h1.left.npl < h1.right.npl:
                tmp_heap = h1.left
                h1.left = h1.right
                h1.right = tmp_heap

            h1.npl = h1.right.npl + 1
        return h1

    def insert(self, v):
        node = TreeNode(v)
        self.root = self.merge(self.root, node)

    def pre_print(self):
        current = self.root
        self.__pre_print(current)
        print '\n',

    def delete_min(self):
        root = self.root
        left_heap = root.left
        right_heap = root.right
        self.root = PriorityQueue.merge(left_heap, right_heap)
        return root.element

    def __pre_print(self, current):
        if not current:
            return
        print current.element,
        self.__pre_print(current.left)
        self.__pre_print(current.right)


def test():
    left_heap = PriorityQueue()
    left_heap.insert(23)
    left_heap.insert(10)
    left_heap.insert(21)
    left_heap.insert(14)
    left_heap.insert(17)
    left_heap.insert(8)
    left_heap.insert(26)
    left_heap.insert(3)
    left_heap.pre_print()
    print left_heap.delete_min()
    left_heap.pre_print()
    left_heap.delete_min()
    left_heap.pre_print()


if __name__ == '__main__':
    test()
