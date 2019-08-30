#
# @lc app=leetcode id=733 lang=python
#
# [733] Flood Fill
#
class Solution(object):

    def dfs(self, r, c, nr, nc):
        self.visited[r][c] = True
        self.image[r][c] = self.newColor
        paths = [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]
        for r, c in paths:
            if 0 <= r < nr and 0 <= c < nc and not self.visited[r][c] and self.image[r][c] == self.startingcolor:
                self.dfs(r, c, nr, nc)
        


    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.image = image
        if not self.image:
            return self.image
        self.newColor = newColor
        self.startingcolor = self.image[sr][sc]
        n = len(self.image)
        m = len(self.image[0])
        self.visited = [[False for _ in range(m)] for _ in range(n)]
        self.dfs(sr, sc, n, m)
        return self.image
        

