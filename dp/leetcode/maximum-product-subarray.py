class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return nums[0]
        dp = [[nums[i], nums[i]] for i in range(n)]
        for i in range(1, n):
            a = dp[i-1][0] * nums[i] 
            b = dp[i-1][1] * nums[i]
            dp[i][0] = max(a, b, nums[i])
            dp[i][1] = min(a, b, nums[i])
        maxes = [item[0] for item in dp]
        return max(maxes)

print Solution().maxProduct([3,-1,4])
print Solution().maxProduct([3,-1,4]) == 4
print Solution().maxProduct([3,-1,4,-4])
print Solution().maxProduct([3,-1,4,-4]) == 48
print Solution().maxProduct([-2,0,-1])
print Solution().maxProduct([-2,0,-1]) == 0
print Solution().maxProduct([0, 2])
print Solution().maxProduct([0, 2]) == 2
print Solution().maxProduct([2,3,-2,4])
print Solution().maxProduct([2,3,-2,4]) == 6



