class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        dp = [float('inf') for i in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i- j*j] + 1)
                j = j + 1
        return dp[n]

print Solution().numSquares(12)
print Solution().numSquares(13)
print Solution().numSquares(43)
print Solution().numSquares(18)
