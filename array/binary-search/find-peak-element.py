class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        print nums
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) / 2
            print 'mid ', mid, nums[mid]
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            if nums[mid - 1] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        # if processing finished, return left
        return left

print Solution().findPeakElement([2,1])