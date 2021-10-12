class Tree(object):

    def __init__(self):
        self.root = None

    def is_empty(self):
        """
        Metoda proverava da li stablo ima elemenata.
        """
        return self.root is None

    def depth(self, x):
        """
        Metoda izračunava dubinu zadatog čvora.

        Argument:
        - `x`: čvor čija dubina se računa
        """
        if x.is_root():
            return 0
        else:
            return 1 + self.depth(x.parent)

