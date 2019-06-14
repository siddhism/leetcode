from collections import defaultdict
class Graph:

    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, value):
        self.graph[u] = {v: value}
        self.graph[v] = {u: float(1) // value}

    def dfs_util(self, u, v, visited, product):
        # traverse dfs upto v and get output
        visited[u] = True
        product = product * self.graph[u][v]
        for neighbour in self.graph[u]:
            if not visited[u]:
                product = product * self.graph[u]
                # TO be continued
                self.dfs_util(neighbour, v, visited, product)
        return product

    def get_edge(self, u, v):
        if u == v:
            return 1
        if u not in self.graph:
            return -1
        if u in self.graph and v not in self.graph[u]:
            return -1
        return self.graph[u][v]

    def print_graph(self):
        for k, v in self.graph.items():
            print k, '-> ', v


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = Graph()
        for i in range(len(equations)):
            eq = equations[i]
            val = values[i]
            g.add_edge(eq[0], eq[1], val)
        # Compute from end to end
        for i in range(len(g.graph)):
            for j in range(len(g.graph)):
                for k in range(len(g.graph)):
                    val = g.get_edge(i, k) * g.get_edge(k, j)
                    g.add_edge(i, j, val)
        g.print_graph()
        for q in queries:
            return g.get_edge(q[0], q[1])
