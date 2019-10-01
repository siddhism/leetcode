#
# @lc app=leetcode id=410 lang=python
#
# [410] Split Array Largest Sum
#
class Solution(object):

    def split(self, arr, largestSum):
        """
        Tells the no. of possible pieces which can make num same as largestSum
        """
        tmp_sum = 0
        pieces = 1
        for num in arr:
            if tmp_sum + num > largestSum:
                # increase num of pieces and start adding from current index
                pieces += 1
                tmp_sum = num
            else:
                tmp_sum += num
        return pieces

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        lo = max(nums)
        hi = sum(nums)
        while lo < hi:
            mid = lo + (hi - lo) / 2
            pieces = self.split(nums, largestSum=mid)
            if pieces > m:
                # means this is a possible answer, search for higher
                lo = mid + 1
            else:
                hi = mid
        return hi

# print Solution().splitArray([7,2,5,10,8],1) 
# print Solution().splitArray([7,2,5,10,8],2) 
# print  Solution().splitArray([7,2,5,10,8],3) 
# print  Solution().splitArray([7,2,5,10,8],4) 
# print  Solution().splitArray([7,2,5,10,8],5) 
# print  Solution().splitArray([1,2,3,4,5], 1) 
# print  Solution().splitArray([1,2147483647], 1) 
# print  Solution().splitArray([1,2147483647], 2) 

