#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#
class Solution(object):
    def solve(self, board):
        queue = collections.deque([])
        self.rows = len(board)
        self.cols = len(board[0])
        for r in xrange(len(board)):
            for c in xrange(len(board[0])):
                if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "O":
                board[r][c] = "D"
                bounds = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

                for next_r, next_c in bounds:
                    if 0 <= next_r < self.rows and 0 <= next_c < self.cols:
                        if board[next_r][next_c] == "O":
                            queue.append((next_r, next_c))
            
        for r in xrange(len(board)):
            for c in xrange(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"