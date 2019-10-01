#
# @lc app=leetcode id=583 lang=python
#
# [583] Delete Operation for Two Strings
#
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #
# @lc app=leetcode id=72 lang=python
#
# [72] Edit Distance
#
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        dp[0][0] = 0
        # fill up first row of dp
        for i in range(1, n+1):
            dp[i][0] = i
        for j in range(1, m+1):
            dp[0][j] = j

        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    # dp cols -1, to consider word cols according to i, j
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1]) + 1
        # print dp
        return dp[n][m]


        

