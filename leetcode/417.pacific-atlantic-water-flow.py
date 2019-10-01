#
# @lc app=leetcode id=417 lang=python
#
# [417] Pacific Atlantic Water Flow
#

class Solution(object):

    def dfs_pacific(self, i, j, visited):
        visited[i][j] = True

        bounds = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]

        for next_r, next_c in bounds:
            next_key = (next_r, next_c)
            if (next_r < 0 or next_r >= self.rows or next_c < 0 or next_c >= self.cols or 
                visited[next_r][next_c] or self.matrix[next_r][next_c] < self.matrix[i][j]):
                continue
            self.dfs_pacific(next_r, next_c, visited)


    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        self.matrix = matrix
        from collections import defaultdict
        self.rows = len(matrix)
        if not matrix:
            return []
        self.cols = len(matrix[0])

        self.pacific = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.atlantic = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        for j in range(self.cols):
            self.dfs_pacific(0, j, self.pacific)
            self.dfs_pacific(self.rows-1, j, self.atlantic)

        for i in range(self.rows):
            self.dfs_pacific(i, 0, self.pacific)
            self.dfs_pacific(i, self.cols - 1, self.atlantic)

        result = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.pacific[i][j] and self.atlantic[i][j]:
                    result.append([i, j])
        return result


