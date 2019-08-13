class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        counts = defaultdict(int)
        counts[0] = 1
        res = 0
        running_sum = 0
        for num in nums:
            running_sum += num
            res += counts.get(running_sum-k, 0)
            counts[running_sum] = counts.get(running_sum, 0) + 1
            print ('counts ', counts, ' res ', res, ' running_sum ', running_sum)
        return res

print Solution().subarraySum([1, 2, 3], 3)