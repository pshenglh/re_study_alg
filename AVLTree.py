from tree import SearchTree, Node

class AVLTree(SearchTree):

    def insert(self, v):
        n = self.root
        self.root = self.__insert(v, n)

    def single_rotate_left(self, n):
        k2 = n
        k1 = n.left
        tmp_node = k1.right
        k1.right = k2
        k2.left = tmp_node

        k2.height = max(self.height(k2.left), self.height(k2.right)) + 1
        k1.height = max(self.height(k1.left), self.height(k2)) + 1

        return k1

    def single_rotate_right(self, n):
        k1 = n
        k2 = n.right
        tmp_node = k2.left
        k2.left = k1
        k1.right = tmp_node

        k1.height = max(self.height(k1.left), self.height(k1.right)) + 1
        k2.height = max(self.height(k1), self.height(k2.right)) + 1

        return k2

    def double_rotate_left(self, n):
        k3 = n
        k1 = k3.left
        k2 = k1.right

        k3.left  = self.single_rotate_right(k3.left)
        return self.single_rotate_left(k3)

    def double_rotate_right(self, n):
        k1 = n
        k3 = n.right
        k2 = k3.left

        k1.right = self.single_rotate_left(k1.right)
        return self.single_rotate_right(k1)

    def __insert(self, v, n):
        if n == self.root and not n.value:
            n.value = v
        elif not n:
            n = Node(v)
        elif v < n.value:
            n.left = self.__insert(v, n.left)
            if self.height(n.left) - self.height(n.right) == 2:
                if v < n.left.value:
                    n = self.single_rotate_left(n)
                else:
                    n = self.double_rotate_left(n)
        elif v > n.value:
            n.right = self.__insert(v, n.right)
            if self.height(n.right) - self.height(n.left) == 2:
                if v > n.right.value:
                    n = self.single_rotate_right(n)
                else:
                    n = self.double_rotate_right(n)
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return n

    def height(self, n):
        if not n:
            return 0
        elif isinstance(n, Node):
            return n.height

def test():
    avlt = AVLTree()
    avlt.insert(4)
    avlt.insert(2)
    avlt.insert(6)
    avlt.insert(1)
    avlt.insert(3)
    avlt.insert(5)
    avlt.insert(7)
    print avlt.root.height
    avlt.pre_traverse()
    avlt.insert(16)
    avlt.insert(15)
    avlt.pre_traverse()
    print avlt.root.height
    avlt.insert(14)
    avlt.pre_traverse()
    avlt.insert(13)
    avlt.pre_traverse()
    avlt.insert(12)
    avlt.pre_traverse()
    print avlt.root.height

if __name__ == '__main__':
    test()
