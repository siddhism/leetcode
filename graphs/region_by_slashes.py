class DSU:

    def __init__(self, N):
        self.parent = {}

    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        self.parent[root_a] = root_b

    def root(self, i):
        self.parent.setdefault(i, i)
        while self.parent[i] != i:
            i = self.parent[i]
        return i


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        dsu = DSU(len(grid))
        for i in range(len(grid)):
            for j in range(len(grid)):
                val = grid[i][j]
                if i:
                    dsu.union((i, j, 0), (i-1, j, 3))
                if j:
                    # Connect right and left of two areas
                    dsu.union((i, j, 1), (i, j-1, 2))
                if val == '/':
                    # connect top right and bottom left
                    dsu.union((i, j, 0), (i, j, 1))
                    dsu.union((i, j, 2), (i, j, 3))
                elif val == '\\':
                    dsu.union((i, j, 0), (i, j, 2))
                    dsu.union((i, j, 1), (i, j, 3))
        # return no. of connected components
        count = sum([dsu.root(x) == x for x in dsu.parent])
        return count