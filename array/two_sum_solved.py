class Solution(object):
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found = {}
        for i in range(len(nums)):
            current = nums[i]
            import ipdb; ipdb.set_trace()
            comp = target - current
            if current in found.keys():
                return [found.get(current), i]
            else:
                found[comp] = i
            print current, found

print Solution().twoSum([3, 2, 4], 6)