#
# @lc app=leetcode id=286 lang=python
#
# [286] Walls and Gates
#

class Solution(object):

    def is_out_of_bound(self, i, j):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return False
        return True

    def dfs(self, i, j):
        # not marking node as visited, as we need to revisit it and update it
        # print i, j, source_value
        # if i == 1 and j == 3:
            # import ipdb; ipdb.set_trace()
        self.visited[i][j] = True

        bounds = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        for next_r, next_c in bounds:
            # print i, j, rooms[i][j], next_r, next_c
            if self.is_out_of_bound(next_r, next_c):
                continue
            neighb_value = self.rooms[next_r][next_c]
            if neighb_value == 0 or neighb_value == -1 or self.visited[next_r][next_c]:
                # don't update the gate itself bhai yaar. also wall.
                continue
            new_value = min(self.rooms[i][j] + 1, neighb_value)
            self.rooms[next_r][next_c] = new_value
            # print ' came here for neighb_value ', neighb_value, 'current neighbs ', next_r, next_c, ' i j ', i, j
        for next_r, next_c in bounds:
            # print i, j, rooms[i][j], next_r, next_c
            if self.is_out_of_bound(next_r, next_c):
                continue
            neighb_value = self.rooms[next_r][next_c]
            if neighb_value == 0 or neighb_value == -1 or self.visited[next_r][next_c]:
                # don't update the gate itself bhai yaar. also wall.
                continue
            self.dfs(next_r, next_c)


    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        self.rooms = rooms
        self.rows = len(rooms)
        self.cols = len(rooms[0])
        self.INF = 2 ** 31 - 1

        #  Need to start from gates always and find dist to it. update it later with min if found from other gate
        queue = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.rooms[i][j] == 0:
                    queue.append((i, j))
        
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        
        # Do a DFS for all nodes starting from first one
        while len(queue) > 0:
            top = queue.pop(0)
            i, j = top
            visited[i][j] = True
            # neighbours of top
            bounds = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

            for next_r, next_c in bounds:
                # print i, j, rooms[i][j], next_r, next_c
                if self.is_out_of_bound(next_r, next_c):
                    continue
                next_value = self.rooms[next_r][next_c]
                if next_value == 0 or next_value == -1 or visited[next_r][next_c]:
                    # don't update the gate itself bhai yaar. also don't hit the wall.
                    continue
                new_value = min(self.rooms[i][j] + 1, next_value)
                self.rooms[next_r][next_c] = new_value

                # add them to bfs layer
                queue.append((next_r, next_c))





# data = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Solution().wallsAndGates(data)
# # print data
# data = [[0,2147483647,-1,2147483647,2147483647,-1,-1,0,0,-1,2147483647,2147483647,0,-1,2147483647,2147483647,2147483647,2147483647,0,2147483647,0,-1,-1,-1,-1,2147483647,-1,-1,2147483647,2147483647,-1,-1,0,0,-1,0,0,0,2147483647,0,2147483647,-1,-1,0,-1,0,0,0,2147483647],[2147483647,0,-1,2147483647,0,-1,-1,-1,-1,0,0,2147483647,2147483647,-1,-1,2147483647,-1,-1,2147483647,2147483647,-1,0,-1,2147483647,0,2147483647,-1,2147483647,0,2147483647,0,2147483647,-1,2147483647,0,2147483647,-1,2147483647,0,2147483647,2147483647,0,-1,2147483647,-1,-1,-1,0,2147483647]]
# m = len(data[0])
# for i in range(len(data)):
#     for j in range(m):
#         print data[i][j] , ' ', 
#     print '\n'
# Solution().wallsAndGates(data)
# print 'now what'
# for i in range(len(data)):
#     for j in range(m):
#         print data[i][j] , ' ', 
#     print '\n'
# expected = [[0,1,-1,2,1,-1,-1,0,0,-1,1,1,0,-1,4,3,2,1,0,1,0,-1,-1,-1,-1,2,-1,-1,1,2,-1,-1,0,0,-1,0,0,0,1,0,1,-1,-1,0,-1,0,0,0,1],[1,0,-1,1,0,-1,-1,-1,-1,0,0,1,1,-1,-1,4,-1,-1,1,2,-1,0,-1,1,0,1,-1,1,0,1,0,1,-1,1,0,1,-1,1,0,1,1,0,-1,1,-1,-1,-1,0,1]]
# for i in range(len(data)):
#     for j in range(m):
#         if not data[i][j] == expected[i][j]:
#             print data[i][j] , ' vs ', expected[i][j], 'row col ', i, j
#     print '\n'
# # [[0,1,-1,2,1,-1,-1,0,0,-1,1,2,0,-1,4,3,2,1,0,1,0,-1,-1,-1,-1,2,-1,-1,1,2,-1,-1,0,0,-1,0,0,0,1,0,2,-1,-1,0,-1,0,0,0,1],[1,0,-1,3,0,-1,-1,-1,-1,0,0,2,1,-1,-1,4,-1,-1,1,2,-1,0,-1,1,0,1,-1,1,0,1,0,1,-1,1,0,1,-1,1,0,1,1,0,-1,1,-1,-1,-1,0,1]]
# [[0,1,-1,2,1,-1,-1,0,0,-1,1,1,0,-1,4,3,2,1,0,1,0,-1,-1,-1,-1,2,-1,-1,1,2,-1,-1,0,0,-1,0,0,0,1,0,1,-1,-1,0,-1,0,0,0,1],[1,0,-1,1,0,-1,-1,-1,-1,0,0,1,1,-1,-1,4,-1,-1,1,2,-1,0,-1,1,0,1,-1,1,0,1,0,1,-1,1,0,1,-1,1,0,1,1,0,-1,1,-1,-1,-1,0,1]]

