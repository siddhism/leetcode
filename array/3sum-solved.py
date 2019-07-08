class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        length = len(nums)
        results = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # if it's same as prev , no need
                continue
            l = i + 1
            r = length - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l = l + 1
                elif sum > 0:
                    r = r - 1
                else:
                    results.append([nums[i], nums[l], nums[r]])
                    # to not process duplicaates
                    while l < r and nums[l] == nums[l+1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r-1]:
                        r = r - 1
                    l = l + 1
                    r = r - 1
        return results


print Solution().threeSum([-1, 2, -2, -1])
