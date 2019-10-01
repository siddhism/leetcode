class DSU(object):

    def __init__(self, N):
        from collections import defaultdict
        self.parent = range(N)
        # defaultdict was not working for 0 index case and weird to handle
        # self.parent = defaultdict(int)
        self.size = defaultdict(int)

    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        if self.size[root_a] < self.size[root_b]:
            self.parent[root_a] = root_b
            self.size[b] += 1
        else:
            self.parent[root_b] = root_a
            self.size[a] += 1
        # without path compression
        # self.parent[root_a] = root_b

    def root(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.root(self.parent[i])
        return self.parent[i]
        # without path compression
        # while self.parent[i] != i:
        #     i = self.parent[i]
        # return i


def kruskalMST(graph, V):
    # graph is given with nodes in form of (u, v , w). source , destination, weight
    i = 0
    e = 0
    V = V # no. of vertices

    dsu = DSU()

    # sort all edges in order of weight
    graph = sorted(graph.items(), key=lambda item: item[2])
    result = []

    # Number of edges to be taken is equal to V-1 
    while e < V - 1:
        # pick element from graph and try to include it
        u, v, w = graph.pop(0) # or can use i here which is auto incrementing
        x = dsu.root(u)
        y = dsu.root(v)

        # if joining these two vertices doesn't form a cycle, join
        if x != y:
            dsu.union(x, y) # can join node or parent, doesn't matter
            result.append((u, v, w))
            e = e + 1 # picked edge count goes up
        
        # else this edge is discarded

    # return sum of weights or result whatever is asked
    return sum([item[2] for item in result])
