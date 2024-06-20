class Node:
    def __init__(self, character, frequency):
        self.char = character
        self.freq = frequency
        self.right = None
        self.left = None

    def get_frequency(self):
        return self.freq

    def add_right(self, node):
        if not self.right:
            self.right = node
        else:
            print("There is already an assigned value.")

    def add_left(self, node):
        if not self.left:
            self.left = node
        else:
            print("There is already an assigned value.")

    # code adapted from https://stackoverflow.com/questions/20242479/printing-a-tree-data-structure-in-python
    def __repr__(self, level=0):
        ret = "\t" * level + f"Node(char={repr(self.char)}, freq={self.freq})\n"
        if self.left:
            ret += self.left.__repr__(level + 1)
        if self.right:
            ret += self.right.__repr__(level + 1)
        return ret


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def get_length(self):
        return len(self.elements)

    def place(self, item, priority):
        self.elements.append((priority, item))
        self.elements.sort(key=lambda x: x[0])

    def get(self):
        return self.elements.pop(0)[1]
