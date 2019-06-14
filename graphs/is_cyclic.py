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

    def is_cyclic_util(self, v, visited, rec_stack):
        print ('Inside is cyclic util for node ', v)
        print ('rec stack is ', rec_stack)
        visited[v] = True
        rec_stack[v] = True

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.is_cyclic_util(neighbour, visited, rec_stack):
                    return True
            elif visited[neighbour] and rec_stack[neighbour]:
                return True

        # the node needs to be popped from recursive stack
        rec_stack[v] = False
        print ('Returning is cyclic util for node ', v)
        print ('rec stack is ', rec_stack)
        return False

    def is_cyclic(self):
        visited = [False for i in range(len(self.graph) + 1)]
        rec_stack = [False for i in range(len(self.graph) + 1)]

        for v in range(self.V):
            print ('Calling is cyclic util for node ', v)
            if not visited[v]:
                if self.is_cyclic_util(v, visited, rec_stack):
                    return True
        return True

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# g = Graph(7)
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(1, 3)
# g.add_edge(1, 4)
# g.add_edge(4, 5)
# g.add_edge(5, 6)
# g.add_edge(6, 4)


print g.is_cyclic()