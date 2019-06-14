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

    def bfs(self, v):
        # create empty visited method
        visited = [False] * (len(self.graph) + 1)

        # mark the first node as visited and push it to queue
        queue = []
        visited[v] = True
        queue.append(v)

        # while queue is not empty, get item from queue and visit it's neighbours
        while queue:
            top = queue[0]
            print top,
            queue = queue[1:]
            for neighbour in self.graph[top]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True



graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

graph.bfs(2)
