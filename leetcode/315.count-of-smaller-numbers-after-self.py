#
# @lc app=leetcode id=315 lang=python
#
# [315] Count of Smaller Numbers After Self
#
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cur_nums = {}
        n = len(nums)
        for i in range(n):
            cur_nums[nums[i]] = i
        # sorted numbers
        sorted_nums = dict(sorted(cur_nums.items(), key=lambda kv: kv[0]))
        # now check orig numbers one by one and check at what index it is
        out = []
        print cur_nums
        for num in nums:
            original_idx = sorted_nums.get(num)
            count = 0
            for index, (k, v) in enumerate(sorted_nums.items()):
                if v > idx:
                    continue
                count += 1
            result = idx - count
            print 'num ', num, ' idx ', idx, ' count ', count, ' result ', result
            out.append(result)
        return out
        

