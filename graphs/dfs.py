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

    def dfs_util(self, v, visited):
        visited[v] = True
        print v,
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                self.dfs_util(neighbour, visited)

    def dfs(self, v):
        visited = [False] * (len(self.graph) + 1)
        visited[v] = True
        self.dfs_util(v, visited)


graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

graph.dfs(2)
