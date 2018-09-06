class Heap(object):

    def __init__(self):
        self.heap = [None]
        self.size = 0

    def insert(self, v):
        self.heap.append(v)
        self.size += 1
        i = self.size
        while i >= 0:
            if self.heap[i/2] > v:
                self.heap[i] = self.heap[i/2]
                i = i / 2
            else:
                break
        self.heap[i] = v

    def del_min(self):
        min_ele = self.heap[1]
        last_ele = self.heap[self.size]
        self.size -= 1

        i = 1
        while (i*2) <= self.size:
            child = i * 2 + 1 if self.heap[i*2+1] < self.heap[i*2] else (i*2)
            if last_ele > self.heap[child]:
                self.heap[i] = self.heap[child]
                i = i * 2
            else:
                break
        self.heap[i] = last_ele
        self.heap.pop(-1)
        return min_ele


def test():
    h = Heap()
    h.insert(10)
    h.insert(13)
    h.insert(5)
    h.insert(3)
    print h.heap
    print h.del_min()
    print h.heap
    print h.del_min()
    print h.heap


if __name__ == '__main__':
    test()
