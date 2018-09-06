class DulNode(object):
    def __init__(self, value, pre=None, next=None):
        self.value = value
        self.pre = pre
        self.next = next

    def __repr__(self):
        return 'Node {}'.format(self.value)


class DoublyLinkedList(object):
    def __init__(self):
        self.header = DulNode(None)

    def add(self, x):
        __current = self.header
        while __current.next:
            __current = __current.next
        __current.next = DulNode(x, __current, None)

    def delete(self, x):
        __current = self.header
        while __current.value != x and __current.next:
            __current = __current.next
        if not __current.next:
            return
        __current.pre.next = __current.next

    def swap_adjacent(self, x):
        current = self.header.next
        while current.value != x:
            current = current.next
        if current.next and current.value == x:
            previous = current.pre
            tmp_node = current.next.next
            previous.next = current.next
            current.next.next = current
            current.next = tmp_node
            previous.next.pre = previous
            current.pre = previous.next
            if tmp_node:
                tmp_node.pre = current

    def reverse_print(self):
        current = self.header
        while current.next:
            current = current.next
        while current.value:
            print current.value,
            current = current.pre
        print '\n'

    def __repr__(self):
        __current = self.header.next
        s = ''
        while __current:
            s += '{} '.format(__current.value)
            __current = __current.next
        return s


def test():
    dl = DoublyLinkedList()
    dl.add(3)
    dl.add(8)
    dl.add(100)
    dl.add(-4)
    print dl
    dl.reverse_print()
    dl.swap_adjacent(100)
    print dl
    dl.reverse_print()
    dl.delete(8)
    print dl
    dl.reverse_print()

if __name__ == '__main__':
    test()
