#
# @lc app=leetcode id=947 lang=python
#
# [947] Most Stones Removed with Same Row or Column
#
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
            # i = self.parent[i]
            # self.parent[i] = i # path compression
            self.parent[i] = self.root(self.parent[i])
        return self.parent[i]


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        # connect all components going row by by row in Left and down positions
        if not stones:
            return 0
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)
        return N - len({dsu.root(x) for x, y in stones})



