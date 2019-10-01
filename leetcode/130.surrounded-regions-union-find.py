#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#
class Solution(object):
    """incomple and confused"""

    def dfs(self, i, j, visited):
        visited[i][j] = True

        bounds = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        for next_r, next_c in bounds:
            if 0 <= next_r < self.rows and 0 <= next_c < self.cols:
                # backtrack and delete all the colors for this path
                if not visited[next_r][next_c]:
                    if self.board[next_r][next_c] == 'O':
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
        from collections import defaultdict
        self.parent = defaultdict(bool)
        self.x = 'X'
        self.o = 'O'
        self.border = '-1'

        for j in range(self.cols):
            print self.board[self.rows-1][j]
            if self.board[0][j] == 'O':
                self.parent[(0, j)] = '-1'
            if self.board[self.rows-1][j] == 'O':
                self.parent[(self.rows-1, j)] = '-1'

        for i in range(self.rows):
            if self.board[i][0] == 'O':
                self.parent[(i, 0)] = '-1'
            if self.board[i][self.cols-1] == 'O':
                self.parent[(i, self.cols-1)] = '-1'


        print self.parent
        self.print_matrix(self.parent)


        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 'O' and not self.visited[i][j]:
                    self.union_find(i, j)

        
    def print_matrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        print '\n start \n'
        for i in range(n):
            for j in range(m):
                print matrix[i][j], ' ', 
            print '\n'
        print '\n Done \n'
                    
    def union_find(self, i, j):
        self.visited[i][j] = True
        current_key = (i, j)
        bounds = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        for next_r, next_c in bounds:
            if not (0 <= next_r < self.rows and 0 <= next_c < self.cols):
                continue
            
            # find parent of 
                        



data = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(data)
print data

data = [["O","O","O"],["O","O","O"],["O","O","O"]]
Solution().solve(data)
print data



    