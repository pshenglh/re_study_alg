class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return 'Node {}'.format(self.value)

class NodeList(object):

    def __init__(self):
        self.head = Node(None)
        self.length = 0

    def add(self, value):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = Node(value)
        self.length += 1

    def is_empty(self):
        return self.head.next == None

    def is_last(self, p):
        return p.next == None

    def find(self, value):
        current_node = self.head.next
        while current_node.value != None and current_node.value != value:
            current_node = current_node.next
        return current_node

    def find_previous(self, value):
        current_node = self.head
        while current_node.next != None and current_node.next.value != value:
            current_node = current_node.next
        if not current_node.next and current_node.value != value:
            return 'Cant Find This Value'
        return current_node

    def swap_adjacent(self, x):
        current = self.head.next
        while current.next and current.value != x:
            current = current.next
        if current.next and current.value == x:
            tmp_node = current.next.next
            previous_node = self.find_previous(x)
            previous_node.next = current.next
            previous_node.next.next = current
            current.next = tmp_node

    def delete(self, value):
        pre_node = self.find_previous(value)
        if pre_node.next.value != None:
            tmp_node = pre_node.next
            pre_node.next = tmp_node.next
            self.length -= 1

    def insert(self, value, p):
        tmp_node = p.next
        p.next = Node(value, tmp_node)

    def print_list(self):
        current_node = self.head.next
        while current_node != None:
            current_node = current_node.next
        print '\n'

    def __repr__(self):
        current_node = self.head.next
        s = ''
        while current_node != None:
            s += '{} '.format(current_node.value)
            current_node = current_node.next
        return s

    def __len__(self):
        return self.length

    def intersection(self, other):
        current = self.head.next
        other_current = other.head.next
        intersection_list = NodeList()
        while current and other_current:
            if current.value == other_current.value:
                intersection_list.add(current.value)
                current = current.next
                other_current = other_current.next
            elif current.value < other_current.value:
                current = current.next
            else:
                other_current = other_current.next

        return intersection_list

    def union(self, other):
        current = self.head.next
        other_current = other.head.next
        union_list = NodeList()
        while current or other_current:
            if not other_current:
                while current:
                    union_list.add(current.value)
                    current = current.next
            elif not current:
                while other_current:
                    union_list.add(other_current.value)
                    other_current = other_current.next
            elif current.value == other_current.value:
                union_list.add(current.value)
                current = current.next
                other_current = other_current.next
            elif current.value < other_current.value:
                union_list.add(current.value)
                current = current.next
            else:
                union_list.add(other_current.value)
                other_current = other_current.next

        return union_list

class Stack(object):

    def __init__(self):
        self.header = Node(None)

    def push(self, x):
        tmp_node = Node(x)
        tmp_node.next = self.header.next
        self.header.next = tmp_node

    def pop(self):
        if self.is_empty():
            return 'empty stack'
        tmp_node = self.header.next
        self.header.next = tmp_node.next
        return tmp_node.value

    def is_empty(self):
        return not self.header.next

    def __repr__(self):
        current = self.header
        s = ''
        while current.next != None:
            current = current.next
            s += '{} '.format(str(current.value))
        return s

def test():
    l1 = NodeList()
    l1.add(2)
    l1.add(5)
    l1.add(6)
    l1.add(-3)
    print l1
    l1.swap_adjacent(5)
    print l1
    l1.delete(5)
    print l1
    l1.insert(10, l1.find(6))
    print l1

def test_stack():
    stack = Stack()
    stack.push(3)
    print stack
    stack.push(5)
    stack.push(10)
    print stack
    print stack.pop()
    print stack
    print stack.pop()
    print stack
    print stack.pop()
    print stack
    print stack.pop()

def test_union_inter():
    l1 = NodeList()
    l2 = NodeList()
    l1.add(1)
    l1.add(3)
    l1.add(5)
    l1.add(23)
    l2.add(3)
    l2.add(5)
    l2.add(10)
    i_l = l1.intersection(l2)
    print i_l
    u_l = l1.union(l2)
    print u_l

if __name__ == '__main__':
    test_union_inter()

