#
# @lc app=leetcode id=305 lang=python
#
# [305] Number of Islands 2
#

class DisjointSet(object):

    def __init__(self, n):
        from collections import defaultdict
        self.parent = {}
        self.size = defaultdict(int)
        self.count = 0
    
    def add(self, node):
        if node in self.parent:
            return
        self.parent[node] = node
        self.size[node] = 1
        self.count += 1

    def union(self, a, b):
        pa = self.root(a)
        pb = self.root(b)
        if pa == pb:
            return
        if self.size[pa] < self.size[pb]:
            self.parent[pa] = pb
            self.size[pb] += self.size[pa]
        else:
            self.parent[pb] = pa
            self.size[pa] += self.size[pb]
        # two elements joined, reduce count
        self.count -= 1

    def root(self, i):
        # get value from parent or get default same as i
        while i != self.parent.get(i, i):
            i = self.parent[i]
        return i

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def get_key(i, j):
            return n * i + m * j

        dsu = DisjointSet(n*m)
        arr = [[0 for _ in range(n)] for i in range(m)]
        num_islands = []
        for land in positions:
            r, c = land
            arr[r][c] = 1
            # here land is = (r, c)
            land_key = (r, c)
            dsu.add(land_key)
            # dsu.parent[land_key] = land_key
            coords = [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]
            for cord in coords:
                nxtr, nxtc = cord
                if 0 <= nxtr < m and 0 <= nxtc < n and arr[nxtr][nxtc]:
                    dsu.union(land_key, cord)
            # current num of islands
            num_islands.append(dsu.count)
        return num_islands


# print Solution().numIslands2(3,3,[[0,0],[0,1],[1,2],[2,1]])



