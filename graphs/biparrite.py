from collections import defaultdict

class Graph:

    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def add_edge(self, u, v):
        self.graph[u].append(v)

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        g = Graph(len(graph))
        for node_index, dests in enumerate(graph):
            for dest in dests:
                g.add_edge(node_index, dest)

        # Initialize color array and set source vertex color
        color = [-1 for _ in range(g.V)]
        color[0] = 1
        queue = []
        queue.append(0)

        while queue:
            u = queue.pop()
            if u in g.graph[u]:
                return False # means self loop

            # check for all neighbours of u
            for node in g.graph[u]:
                print 'For node u ', color[node]
                # if visited[node]:
                #     continue
                if color[node] == -1:
                    color[node] = 1 -  color[u] # set opposite to current vertex
                    queue.append(node)
                elif color[node] == color[u]:
                    return False
        return True

