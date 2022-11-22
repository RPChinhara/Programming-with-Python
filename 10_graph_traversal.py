from collections import deque

class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def dfs(self, vertex, visited = None):
        if visited is None:
            visited = set()
        visited.add(vertex)
        print(vertex, end=" ")
        for next in self.gdict[vertex] - visited:
            self.dfs(next, visited)
        return visited

    def bfs(self, startnode):
        seen, queue = set([startnode]), deque([startnode])
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            for node in self.gdict[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)

gdict = graph({ 
    "a" : set(["b","c"]),
    "b" : set(["a", "d"]),
    "c" : set(["a", "d"]),
    "d" : set(["e"]),
    "e" : set(["a"])
})

print("Depth First Traversal: ")
gdict.dfs("a")
print('\n')

print("Breadth First Traversal: ")
gdict.bfs("a")
print('\n')
