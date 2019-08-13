
#         2   1    1   2

#     0   0   0    0   0

# 2   0   2   2    3   4   

# 1   0   0   1    1   2

# 1   0   0   0    1   2  

# 2   0   0   0    0   2  


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        dp = [nums[i] for i in range(n)]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]
        # nums = [0] + nums
        # # cum = [nums[i] for i in range(n)]
        # dp = [[0 for i in range(n+1)] for _ in range(n+1)]
        # dp[1][1] = nums[0]
        # for i in range(1, n+1):
        #     for j in range(2, n+1):
        #         if j < i:
        #             dp[i][j] = 0
        #         else:
        #             dp[i][j] = max(dp[i][j-2] + nums[j], dp[i][j-1])
        #         print i, j, dp[i][j]
        # print dp
        # return max(dp[i][n] for i in range(n))

print Solution().rob([2,1,1,2])
