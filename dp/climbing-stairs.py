class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n+1)]
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        # print dp
        return dp[n]

print Solution().climbStairs(2)
print Solution().climbStairs(3)
print Solution().climbStairs(4)
print Solution().climbStairs(5)
