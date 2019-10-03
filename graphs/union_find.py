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
        # with path compressoin
        if self.parent[i] != i:
            self.parent[i] = self.root(self.parent[i])
        return self.parent[i]
        # alt version (try) # create recursion stack to understand 5 -> root(4) -> root(3)
        # if self.parent[i] == i:
        #     return i
        # self.parent[i] = self.root(self.parent[i])
        # return self.parent[i]
        # without path compression
        # while self.parent[i] != i:
        #     i = self.parent[i]
        # return i


union(0, 1)
union(1, 2)
union(4, 5)
union(0, 1)
union(0, 1)
