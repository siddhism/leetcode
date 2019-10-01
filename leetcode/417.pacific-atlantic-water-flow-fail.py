#
# @lc app=leetcode id=417 lang=python
#
# [417] Pacific Atlantic Water Flow
#

class Node(object):

    def __init__(self, value, x, y):
        self.x = x
        self.y = y
        self.value = value

class Solution(object):

    def dfs_pacific(self, i, j, visited):
        visited[i][j] = True

        bounds = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]

        for next_r, next_c in bounds:
            next_key = (next_r, next_c)
            if (next_r < 0 or next_r >= self.rows or next_c < 0 or next_c >= self.cols or 
                self.matrix[next_r][next_c] < self.matrix[i][j]):
                continue
            self.dfs_pacific(next_r, next_c, visited)

            # # print 'next node ', next_key
            # visited[next_key] = True

            # nxt = self.matrix[next_r][next_c]
            # # if neighbour is pacific, you are pacific
            # if self.pacific[next_key] and nxt <= current:
            #     self.pacific[current_key] = True
            #     # self.dfs_pacific(i, j)

            # if self.atlantic[next_key] and nxt <= current:
            #     self.atlantic[current_key] = True
            #     # self.dfs_pacific(i, j)


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

        # # visit all elements one by one
        # for i in range(self.rows):
        #     for j in range(self.cols):
        #         if not self.visited[(i, j)]:
        #             self.dfs_pacific(i, j)
        #         # print 'one round done ', self.visited

        # self.visited = defaultdict(bool)
        # for i in range(self.rows-1, 0, -1):
        #     for j in range(self.cols-1, 0, -1):
        #         if not self.visited[(i, j)]:
        #             self.dfs_pacific(i, j)

        for i in range(self.rows):
            for j in range(self.cols):
                print matrix[i][j], ' ', 
            print '\n'

        print 'pacific data \n',

        for i in range(self.rows):
            for j in range(self.cols):
                print self.pacific[i][j], ' ', 
            print '\n'

        print 'atlantic data \n',
        for i in range(self.rows):
            for j in range(self.cols):
                print self.atlantic[i][j], ' ', 
            print '\n'

        result = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.pacific[i][j] and self.atlantic[i][j]:
                    result.append([i, j])
        return result

print Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])

# atl data  [(4, 0), (4, 4), (4, 1), (0, 4), (1, 4), (4, 2), (2, 4), (4, 3), (3, 4)]
# pac data  [(3, 0), (0, 3), (4, 0), (0, 0), (0, 4), (1, 0), (0, 1), (2, 0), (0, 2)]
# [[4, 0], [0, 4]]


