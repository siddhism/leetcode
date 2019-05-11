from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_edges(self):
        for node, adj in self.graph.items():
            print node, ' -> '
            for item in adj:
                print item,


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 0)
g.add_edge(1, 3)
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 1)
g.add_edge(2, 3)

g.add_edge(3, 1)
g.add_edge(3, 2)
g.add_edge(3, 4)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(4, 3)

g.print_edges()
