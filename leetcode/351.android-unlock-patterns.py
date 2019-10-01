#
# @lc app=leetcode id=351 lang=python
#
# [351] Android Unlock Patterns
#
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = []
        row1 = [1 for _ in range(9)]
        dp.append(row1)
        # put multiply factor for different type of coords
        # mul = [5,5,5,5,7,7,7,7,1]
        row2 = [5,5,5,5,7,7,7,7,8]
        row2 = [5,7,5,7,8,7,5,7,5]
        dp.append(row2)
        # row2 = [5,7,8]
        a = 5
        b = 7
        c = 8
        result = 0
        for i in range(2, n):
            corner = (a+a+a+a+c) * 4
            mids = (a+a+a+a+b+b+c) * 4
            center = 8
            result = corner + mids + center
            print ' i + 1 ', i+1, ' result ', result
        return result
        # return ans

print Solution().numberOfPatterns(1, 2)
print Solution().numberOfPatterns(1, 3)
print Solution().numberOfPatterns(1, 4)
print Solution().numberOfPatterns(2, 4)

