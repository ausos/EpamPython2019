"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""


from collections import deque


class GraphIterator:
    def __init__(self, graph):
        self.E = graph.E
        self.visited = list()
        self.queue = deque()
        if self.E:
            vertex = list(self.E)[0]
            self.visited.append(vertex)
            self.queue.append(vertex)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.queue:
            raise StopIteration
        vertex = self.queue.popleft()
        for i in self.E[vertex]:
            if i not in self.visited:
                self.queue.append(i)
                self.visited.append(i)
        return vertex

class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        return GraphIterator(self)


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertex in graph:
    print(vertex)