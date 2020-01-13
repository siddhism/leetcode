#
# @lc app=leetcode id=221 lang=python
#
# [221] Maximal Square
#
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        matrix = [[int(matrix[i][j]) for j in range(m)] for i in range(n)]
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        result = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    result = max(dp[i][j], result)

        self.print_matrix(matrix)
        self.print_matrix(dp)

        return result * result

    def print_matrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        print '\n start \n'
        for i in range(n):
            for j in range(m):
                print matrix[i][j], ' ', 
            print '\n'
        print '\n Done \n'
            




print Solution().maximalSquare(
    [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
)
# print Solution().maximalSquare(
#     [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
# )
# print Solution().maximalSquare(
#     [["0","1","1","0","1"],["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["0","0","0","0","0"]]
# )
