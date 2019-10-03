#
# @lc app=leetcode id=246 lang=python
#
# [246] Strobogrammatic Number
#

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        remap = {'0': '0', '1':'1', '6': '9', '8': '8', '9': '6'}
        new_s = ''
        for i, c in enumerate(num):
            if c not in remap.keys():
                # immediate break condition, it can never be the number you want
                return False
            new_s += remap[c]
        # reverse it
        new_s = new_s[::-1]
        # check if it's equal
        # print 'num ', num, ' new_s', new_s
        return new_s == num

                


# # 
# print Solution().isStrobogrammatic('10')
# print Solution().isStrobogrammatic('69')
# print Solution().isStrobogrammatic('101')
# print Solution().isStrobogrammatic('6969')
# print Solution().isStrobogrammatic('1698691')
# print Solution().isStrobogrammatic('1239')
# print Solution().isStrobogrammatic('6996')
# print Solution().isStrobogrammatic('69969')
# print Solution().isStrobogrammatic('16989618')



        