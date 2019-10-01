#
# @lc app=leetcode id=788 lang=python
#
# [788] Rotated Digits
#
class Solution(object):
    def is_good(self, N):
        N = str(N)
        n = len(N)
        # print N, 
        rev = ''
        # rotate each digit individually by 180
        for i in range(n):
            # if N[i] in '347':
            #     return False
            if N[i] in '018':
                rev += N[i]
            if N[i] == '6':
                rev += '9'
            if N[i] == '9':
                rev += '6'
            if N[i] == '2':
                rev += '5'
            if N[i] == '5':
                rev += '2'
        # print rev, N!=rev
        return N == rev

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        out = []
        for i in range(N+1):
            x = str(i)
            if '3' in x or '4' in x or '7' in x:
                continue
            if not self.is_good(i):
                out.append(i)
        # print 'out put ', out
        return len(out)

