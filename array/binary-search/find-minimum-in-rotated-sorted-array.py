class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return nums[0]
        l = 0
        r = n - 1
        while l < r:
            mid = (l + r)/ 2
            # print 'l ', l, 'r ', r, ' mid ', mid
            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            elif nums[l] <= nums[mid]:
                # sorted on left side, search pivot on the right
                l = mid + 1
            else:
                r = mid
        if l == r:
            # means array is sorted, return first element
            return nums[0]
        return nums[r]

print Solution().findMin([2,3,4,5,1])
