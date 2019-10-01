#
# @lc app=leetcode id=334 lang=python
#
# [334] Increasing Triplet Subsequence
#
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78995/Python-Easy-O(n)-Solution
        # read comments in above thread to understand
        n = len(nums)
        first = float('inf')
        second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True

        return False
        
# print Solution().increasingTriplet([1,2,3,4,5])
# print Solution().increasingTriplet([1,4,2,3,0,7])
# print Solution().increasingTriplet([0,4,2,1,0,-1,-3])
# print Solution().increasingTriplet([5,1,5,5,2,5,4])



