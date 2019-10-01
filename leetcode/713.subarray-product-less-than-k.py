#
# @lc app=leetcode id=713 lang=python
#
# [713] Subarray Product Less Than K
#
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        products = []
        product = 1
        l = 0
        r = 0
        count = 0
        if len(nums) == 1:
            if nums[0] < k:
                return 1
            else:
                return 0
        n = len(nums) - 1
        product = 1
        while r <= n and l <= r:
            print 'l , r ', l, r, ' product ' , product
            while product < k and r <= n:
                count += 1
                product = product * nums[r]
                print 'after expanding ', ' l ', l, ' r ', r, ' count ', count, ' product ', product
                r += 1
            # product = product / nums[l - 1]
            l = l + 1 # increase l
            # r = r - 1 # descrease r
            r = l
            product = 1
            # print 'after expand done', ' l ', l,  ' r ', r, ' count ', count, ' product ', product
            # while product < k and l < r:
            #     count += 1
            #     product = product / nums[l-1]
            #     print 'after contracting', ' l ', l,  ' r ', r, ' count ', count, ' product ', product
            #     l += 1
            # l += 1
        return count


print Solution().numSubarrayProductLessThanK([10,5,2,6], 100)
