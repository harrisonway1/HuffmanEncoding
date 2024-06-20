from NodeandPriorityQueueClasses import Node
from NodeandPriorityQueueClasses import PriorityQueue

file = open("example_text.txt", "r")
text = file.read()


class HuffmanEncoding:
    def __init__(self, input_text):
        self.text = input_text
        self.dictionary = {}
        self.codes = {}
        self.queue = PriorityQueue()
        self.root = None

    def update_frequencies(self):
        for letter in self.text:
            if letter in self.dictionary:
                self.dictionary[letter] += 1
            else:
                self.dictionary[letter] = 1

    def create_priority_queue(self):
        for character, frequency in self.dictionary.items():
            node = Node(character, frequency)
            self.queue.place(node, frequency)

    def create_the_tree(self):
        while self.queue.get_length() > 1:
            node1 = self.queue.get()
            node2 = self.queue.get()
            merged_node = Node(None, (node1.get_frequency() + node2.get_frequency()))
            merged_node.add_left(node1)
            merged_node.add_right(node2)
            self.queue.place(merged_node, merged_node.get_frequency())
        self.root = self.queue.get()
        return self.root

    def generate_codes(self, top):
        self.__generate_codes(top, "")

    def __generate_codes(self, node, code):
        if node is None:
            return
        elif node.char is not None:
            self.codes[node.char] = code
            return
        self.__generate_codes(node.left, code + "0")
        self.__generate_codes(node.right, code + "1")

    def __repr__(self):
        return repr(self.root)

    def main(self):
        self.update_frequencies()
        self.create_priority_queue()
        start = self.create_the_tree()
        self.generate_codes(start)


huffman_tree_example = HuffmanEncoding(text)
huffman_tree_example.main()
print(repr(huffman_tree_example))
print(huffman_tree_example.codes)
