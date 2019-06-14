from collections import defaultdict

class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_edge(self):
        for node, adj in self.graph.items():
            print node, ' -> ', adj


graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)



def dfs(g, v):
    s = []
    visited = [False] * (len(g.graph) + 1)
    s.append(v)
    visited[v] = True
    while s:
        top = s[-1]
        print top
        s = s[:-1]
        visited[top] = True
        for node in g.graph[top]:
            if visited[node] == False:
                s.append(node)



dfs(graph, 2)


