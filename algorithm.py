from trie import Node

cars = set()

with open("carros.txt", "r") as file:
    for line in file:
        line = line.strip()[:-1]
        year, brand, model = eval(line)
        cars.add(brand + ' ' + model)

trie = Node()

for car in cars:
    trie.insert(word=car)

nodes = trie.search(query="Dodge Ram")

words = [node.word for node in nodes]

for word in words:
    print(word)