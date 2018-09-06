from List import NodeList

class BinNode(object):

    def __init__(self, element, left=None, sibling=None):
        self.element = element
        self.left = left
        self.sibling = sibling

    def __repr__(self):
        return '<BinNode %r>' % self.element


class BinTree(object):

    def __init__(self):
        self.list = NodeList()

    
