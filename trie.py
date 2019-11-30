import collections


class Trie:
    def __init__(self, data):

        self.trie = Node()

        with open(data, "r") as file:
            for line in file:
                line = line.strip()[:-1]
                year, brand, model = eval(line)
                word = brand + ' ' + model
                self.trie.insert(word.lower())

                if(len(model) > 5):
                    self.trie.insert(model.lower())

    def search(self, query):
        nodes = self.trie.search(query)
        words = [node.word.capitalize() for node in nodes]
        return words


class Node:
    def __init__(self):
        self.children = {}
        self.word = None

    def insert(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter]
        node.word = word
        return node

    def search(self, query):
        node = self
        for letter in query:
            child = node.children.get(letter)
            if child:
                node = child
            else:
                break

        return list(node.get_descendant_nodes())

    def __repr__(self):
        return f'< children: {list(self.children.keys())}, word: {self.word} >'

    def get_descendant_nodes(self):
        que = collections.deque()
        for letter, child_node in self.children.items():
            que.append((letter, child_node))
        while que:
            letter, child_node = que.popleft()
            if child_node.word:
                yield child_node
            for letter, grand_child_node in child_node.children.items():
                que.append((letter, grand_child_node))
