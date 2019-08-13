class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        n = 9
        m = 9
        box = defaultdict(dict)
        row = defaultdict(list)
        col = defaultdict(list)
        for i in range(9):
            for j in range(9):
                box[i][j] = []
        valid = True
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item == '.':
                    continue
                if item in row[i]:
                    valid = False
                    break
                if item in col[j]:
                    valid = False
                    break
                if item in box[i/3][j/3]:
                    valid = False
                    break
                row[i].append(item)
                col[j].append(item)
                box[i/3][j/3].append(item)
        print row.values()
        print col.values()
        print box.values()
        return valid

print Solution().isValidSudoku(
    [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])

print Solution().isValidSudoku(
    [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])