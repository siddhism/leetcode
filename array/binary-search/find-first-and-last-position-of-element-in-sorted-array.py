class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        n = len(nums)
        if n == 0:
            return [-1, -1]
        right = n - 1
        start = -1
        while left + 1 < right:
            mid = (left + right)/2
            print 'left ', left, ' right ', right, ' mid ', mid
            if nums[mid] == target:
                # check for it's left
                start = mid
                right = mid  # this is important to make it terminate
            elif nums[mid] < target:
                # keep going right
                left = mid + 1
            else:
                # keep moving left until it's last element
                right = mid

        # set first of right/left which match target as start
        if nums[right] == target:
            start = right
        if nums[left] == target:
            start = left

        left = 0
        right = n - 1
        end = start # end is by default same as start
        while left + 1 < right:
            mid = (left + right)/2
            # print 'left ', left, ' right ', right, ' mid ', mid
            if nums[mid] == target:
                # check for it's left?
                end = mid
                left = mid
            elif nums[mid] > target:
                # go left
                right = mid
            else:
                # keep moving right until it's last element
                left = mid

        if nums[left] == target:
            end = left
        if nums[right] == target:
            end = right

        return [start, end]

print Solution().searchRange([1, 4], 4)
print Solution().searchRange([1, 4], 1)
print Solution().searchRange([1, 1], 1)
print Solution().searchRange([1, 4], 2)

print Solution().searchRange([5,7,7,8,8,10], 8)
