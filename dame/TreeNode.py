class TreeNode(object):


    __slots__ = 'parent', 'children', 'data','score'

    def __init__(self, data):

        self.parent = None
        self.children = []
        self.data = data


    def is_root(self):

        return self.parent is None

    def is_leaf(self):

        return len(self.children) == 0

    def add_child(self, x):

        # kreiranje dvosmerne veze između čvorova
        x.parent = self
        self.children.append(x)
