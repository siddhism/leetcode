#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#
class Solution(object):

    def dfs(self, i, j, visited, color_type):
        current = self.board[i][j]
        if color_type == self.border and current in [self.o, self.border]:
            visited[i][j] = True
            self.board[i][j] = self.border
        elif color_type == self.o and current == self.o:
            visited[i][j] = True
        # self.board[i][j] = color_type

        bounds = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        for next_r, next_c in bounds:
            if 0 <= next_r < self.rows and 0 <= next_c < self.cols:
                if not visited[next_r][next_c]:
                    nxt = self.board[next_r][next_c]
                    if nxt == color_type:
                        self.dfs(next_r, next_c, visited, color_type)
                    elif color_type == self.border and nxt == self.o:
                        # for border visit nearby zeroes as well
                        self.dfs(next_r, next_c, visited, color_type)

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
        self.x = 'X'
        self.o = 'O'
        self.border = '-1'
        visited_border = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        visited_main = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        for j in range(self.cols):
            print self.board[self.rows-1][j]
            if self.board[0][j] == 'O':
                self.board[0][j] = '-1'
            if self.board[self.rows-1][j] == 'O':
                self.board[self.rows-1][j] = '-1'

        for i in range(self.rows):
            if self.board[i][0] == 'O':
                self.board[i][0] = '-1'
            if self.board[i][self.cols-1] == 'O':
                self.board[i][self.cols-1] = '-1'

        # self.print_matrix(self.board)


        for i in range(self.rows):
            for j in range(self.cols):
                if not visited_border[i][j] and self.board[i][j] == self.border:
                    self.dfs(i, j, visited_border, self.border)

        # # mark them with border color
        # for i in range(self.rows):
        #     for j in range(self.cols):
        #         if visited_border[i][j]:
        #             self.board[i][j] = self.border

        for i in range(self.rows):
            for j in range(self.cols):
                if not visited_main[i][j] and self.board[i][j] == self.o:
                    self.dfs(i, j, visited_main, self.o)

        # mark O -> X and -1 -> O
        for i in range(self.rows):
            for j in range(self.cols):
                if visited_main[i][j]:
                    self.board[i][j] = self.x
                if visited_border[i][j]:
                    self.board[i][j] = self.o


        # print 'border visited'
        # self.print_matrix(visited_border)
        # print 'main visited'
        # self.print_matrix(visited_main)
        print 'new board'
        self.print_matrix(self.board)

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
                        



# data = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Solution().solve(data)
# print data

# data = [["O","O","O"],["O","O","O"],["O","O","O"]]
# Solution().solve(data)
# print data



    