class Graph:
    def __init__(self):
        self.graph = dict()

    # edges are represented as {Node1: (Node2, Weight1), Node2: (Node3, Weight2)}
    def add(self, node, child, weight):
        self.graph[node] = (child, weight)

    def display(self):
        print(self.graph)

obj = Graph()
obj.add(0, 1, 1)
obj.add(1, 2, 3)
obj.display()