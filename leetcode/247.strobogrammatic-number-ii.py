#
# @lc app=leetcode id=247 lang=python
#
# [247] Strobogrammatic Number - 2
#
class Solution(object):
    """https://leetcode.com/problems/strobogrammatic-number-ii/discuss/67275/Python-recursive-solution-need-some-observation-so-far-97"""

    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        rev = ''
        n = len(num)
        # print num, 
        for i in range(n-1, -1, -1):
            if num[i] in '23457':
                return False
            if num[i] in '018':
                rev += num[i]
            if num[i] == '6':
                rev += '9'
            if num[i] == '9':
                rev += '6'
        # print rev            
        return num == rev


    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        evenMidCandidate = ["11","69","88","96", "00"]
        oddMidCandidate = ["0", "1", "8"]
        if n == 1:
            return oddMidCandidate
        if n == 2:
            return evenMidCandidate[:-1]
        if n % 2:
            pre, midCandidate = self.findStrobogrammatic(n-1), oddMidCandidate
        else: 
            pre, midCandidate = self.findStrobogrammatic(n-2), evenMidCandidate
        premid = (n-1)/2
        return [p[:premid] + c + p[premid:] for c in midCandidate for p in pre]