#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#
class Solution(object):

    def dfs(self, i, j, visited):
        visited[i][j] = True

        bounds = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        for next_r, next_c in bounds:
            if 0 <= next_r < self.rows and 0 <= next_c < self.cols:
                # backtrack and delete all the colors for this path
                if not visited[next_r][next_c]:
                    if self.board[next_r][next_c] == '0':
                        self.board[next_r][next_c] = 'X' # change color
                        child_dfs_result = self.dfs(next_r, next_c, visited)
                        # if child returned false, reset
                        if not child_dfs_result:
                            self.board[next_r][next_c] = 'O'
                            return False
            else:
                # if current node was 'O' and we reached boundary, return false
                if self.board[i][j] == 'O':
                    return False
        
        # default return
        return True


    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # we will do dfs from each 0 node
        # if it marks a succusful surrounded region go ahead and color it
        # else mark it -1 or visited so that those are not visited again for coloring
        if not board:
            return
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        color = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        # for i in range(self.rows):
        #     for j in range(self.cols):
        #         if not visited[i][j] and self.board[i][j] == 'O':
        #             is_surrounded = self.dfs(i, j, visited)
        #             if is_surrounded:
        #                 self.board[i][j] = 'X' 

        queue = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 'O':
                    queue.append((i, j))
                    visited[i][j] = True
                    break
        
        while len(queue) > 0:
            top = queue.pop(0)
            i, j = top[0], top[1]
            visited[i][j] = True
            color[i][j] = True

            bounds = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for next_r, next_c in bounds:
                if 0 <= next_r < self.rows and 0 <= next_c < self.cols:
                    if self.board[next_r][next_c] == 'O':
                        if not visited[next_r][next_c]:
                            queue.append((next_r, next_c))
                        elif not color[next_r][next_c]:
                            # if neighbour has warning
                            color[i][j] = False
                else:
                    # if current element was zero it's an empty open end
                    color[i][j] = False
        print color
        data = []
        for i in range(self.rows):
            for j in range(self.cols):
                if color[i][j] and self.board[i][j] == 'O':
                    self.board[i][j] = 'X'
                    
                        



# data = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Solution().solve(data)
# print data

# data = [["O","O","O"],["O","O","O"],["O","O","O"]]
# Solution().solve(data)
# print data

