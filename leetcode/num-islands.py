class Solution(object):
    
    def dfs(self, r, c, nr, nc, grid):
        # visit all nearby islands
        visited[(r, c)] = True
        bounds = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
        for next_r, next_c in bounds:
            key = (next_r, next_c)
            if 0 <= next_r < nr and 0 <= next_c < nc and not visited[key] and grid[r][c] == 1:
                self.dfs(next_r, next_c, nr, nc, grid)


    def numIslands(self, grid):
        from collections import defaultdict
        if not grid:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        visited = defaultdict(bool)
        ans = 0
        for i in range(nr):
            for j in range(nc):
                if not visited[(i, j)] and grid[i][j] == 1:
                    self.dfs(i, j, nr, nc, grid)
                    ans = ans + 1
        
        return ans