from List import NodeList

def Josephus_problem(m, n):
    m_list = NodeList()
    for i in range(1, n+1):
        m_list.add(i)
    current = m_list.head.next

    while len(m_list) > 1:
        for i in range(m):
            if not current.next:
                current = m_list.head.next
            else:
                current = current.next
        m_list.delete(current.value)
        if not current.next:
            current = m_list.head.next
        else:
            current = current.next

    return m_list.head.next.value

def test():
    print Josephus_problem(2, 5)

if __name__ == '__main__':
    test()