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
        rev = ''
        n = len(num)
        print num, 
        for i in range(n-1, -1, -1):
            if num[i] in '23457':
                return False
            if num[i] in '018':
                rev += num[i]
            if num[i] == '6':
                rev += '9'
            if num[i] == '9':
                rev += '6'
        print rev            
        return num == rev

                


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



        