class DSU:

    def __init__(self):
        self.parent = {}

    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
        if i == self.parent[i]:
            return i
        return self.find(self.parent[i])

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        self.parent[root_a] = root_b


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # we have to return edge which is causing to make a cycle
        dsu = DSU()
        for edge in edges:
            a, b = edge[0], edge[1]
            root_a = dsu.find(a)
            root_b = dsu.find(b)
            if root_a == root_b:
                return edge
            dsu.union(a, b)
        return -1 # all nodes connected, no cycle found
