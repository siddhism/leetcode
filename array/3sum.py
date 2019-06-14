class Solution(object):
    def twoSum(self, nums, sum):
        """
        :type nums: List[int]
        :rtype: (int, int)
        """
        # two sum technique to find sum as desired num
        l = 0
        r = len(nums) - 1
        output = []
        while l < r:
            if nums[l] + nums[r] == sum:
                output.append((nums[l], nums[r]))
                l = l + 1
                r = r - 1
            elif nums[l] + nums[r] > sum:
                r = r - 1
            else:
                l = l + 1
        return output

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        results = []
        for i in range(len(nums)-2):
            current = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            two_sum = self.twoSum(nums[i:], -(current))
            # print 'i ', i, ' current ', -(current), 'two_sum ', two_sum
            if two_sum:
                for item in two_sum:
                    output = sorted([-current, item[0], item[1]])
                    if output not in results:
                        results.append(output)
        return results

print Solution().threeSum([1,2,-2,-1])