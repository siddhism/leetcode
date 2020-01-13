#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # pad by 2
        pre = [1 for _ in range(n+2)]
        post = [1 for _ in range(n+2)]
        # fill pre
        for i in range(n):
            pre[i] = nums[i] * pre[i-1]
        print (pre)
        # fill post
        for i in range(n, 0, -1):
            post[i] = post[i] * nums[i]
        print (post)
        # at each index, product except self is pre[i-1] * post[i+1]
        output = []
        for i in range(1, n+1):
            res = pre[i-1] * post[i+1]
            output.append(res)
        return output
        
# @lc code=end

