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
        rank = {val: i + 1 for i, val in enumerate(sorted(set(nums)))}
        N = len(nums)
        res = []
        bit = [0] * (N + 1)
        print rank

        def update(i):
            while i <= N:
                bit[i] += 1
                i = i + (i & -i)
        
        def get_sum(i):
            s = 0
            while i > 0:
                s += bit[i]
                i = i - (i & -i)
            return s

        print ' bit init ' , bit 
        for x in reversed(nums):
            smaller = get_sum(rank[x] - 1)
            update(rank[x])
            # print 'x ', x
            # print 'smaller than x ', x, ' -> ', smaller
            print ' updated bit ', bit
            res.append(smaller)
        return res[::-1]        

print Solution().countSmaller([5,2,6,1])






        

