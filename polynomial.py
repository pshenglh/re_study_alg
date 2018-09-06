class Monomial(object):
    def __init__(self, coefficient, exponent, next=None):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

    def __repr__(self):
        return '{}x^{}'.format(self.coefficient, self.exponent)

class Polymial(object):
    def __init__(self, monomial_list):
        if not monomial_list:
            raise ArithmeticError
        monomial_list.sort(key=lambda l: l[1], reverse=True)
        self.header = Monomial(monomial_list[0][0], monomial_list[0][1])
        for mono in monomial_list[1:]:
            self.add_mono(mono[0], mono[1])

    def add_mono(self, coefficient, exponent):
        self.current = self.header
        while self.current.next != None:
            self.current = self.current.next
        self.current.next = Monomial(coefficient, exponent)

    def __repr__(self):
        self.current = self.header
        ploy_str = ''
        while self.current != None and self.current.coefficient != 0:
            ploy_str += '{}x^{}'.format(self.current.coefficient, self.current.exponent)
            if self.current.next != None:
                ploy_str += ' + '
            self.current = self.current.next
        return ploy_str

    def __mul__(self, other):
        self.current = self.header
        __new_poly_list = []

        while self.current != None:
            other_current = other.header
            while other_current != None:
                new_coefficient = self.current.coefficient * other_current.coefficient
                new_exponent = self.current.exponent * other_current.exponent
                __new_poly_list.append((new_coefficient, new_exponent))
                other_current = other_current.next
            self.current = self.current.next

        new_poly = Polymial(__new_poly_list)
        new_poly.merge()

        return new_poly

    def merge(self):
        self.current = self.header
        while self.current != None and self.current.next != None:
            if self.current.exponent == self.current.next.exponent:
                self.current.coefficient += self.current.next.coefficient
                self.current.next = self.current.next.next
            else:
                self.current = self.current.next


def test():
    poly1 = Polymial([(1,1), (2,3), (10,6), (5,10), (9,100)])
    poly2 = Polymial([(2,2), (10,4), (2,5), (6,15), (9,21)])
    print poly1
    print poly2
    print poly1 * poly2

if __name__ == '__main__':
    test()



