#
# @lc app=leetcode id=947 lang=python
#
# [947] Most Stones Removed with Same Row or Column
#
class DSU(object):

    def __init__(self):
        from collections import defaultdict
        self.parent = defaultdict(int)
        self.size = defaultdict(int)

    def union(a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        if self.size[a] < self.size[b]:
            self.parent[root_a] = root_b
            self.size[b] += 1
        else:
            self.parent[root_b] = root_a
            self.size[a] += 1

    def root(i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        # connect all components going row by by row in Left and down positions
        if not stones:
            return 0
        from collections import defaultdict
        self.graph = defaultdict(list)
        # create graph for which stone is connected to which. check for each stone
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0] == y[0] or x[1] == y[1]:
                    self.graph[i].append(j)
                    self.graph[j].append(i)
        
        # start dfs from first stone
        N = len(stones)
        self.visited = [False for _ in range(N)]
        self.ans = 0

        def dfs(i):
            # r, c = stones[i]
            # mark it visited
            self.visited[i] = True
            self.ans += 1
            for nxt in self.graph[i]:
                if not self.visited[nxt]:
                    dfs(nxt)

        for i, stone in enumerate(stones):
            if not self.visited[i]:
                dfs(i)
                # size of every connected component - 1
                self.ans -= 1
        return self.ans

