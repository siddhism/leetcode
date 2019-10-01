#
# @lc app=leetcode id=1055 lang=python
#
# [1055] Shortest way to form string

class Solution(object):

    def get_min_match(self, source, target):
        print ' Get min match called with ', 'source ',  source, ' target ', target
        ns = len(source)
        nt = len(target)
        i = nt - 1
        j = ns - 1
        if target == '':
            ans = 1
        elif target and source == '':
            # entire source finished to match your fucker target
            ans = len(target)
        else:
            # print ' target ', target[i], ' source ', source[j]
            if target[i] == source[j]:
                # either remaining source matches remaining t
                ans = self.get_min_match(source[:-1], target[:-1])
            else:
                ans = self.get_min_match(source[:-1], target)
        print 'Returning ********** '
        print 'source ', source, ' target ', target, ' returning ', ans 
        return ans

    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        ns = len(source)
        nt = len(target)
        # dp = [[0 for _ in range(source)] for _ in range(target)]
        # print dp
        i = len(target) - 1
        j = len(source) - 1
        res = 0
        # i = len(target) - 1
        ans = len(target) - 1
        while ans != -1:
            ans = self.get_min_match(source, target[:ans])
            res += 1
        return res
        # while i > 1:
        #     ans = self.get_min_match(source, target[:i])
        #     if ans == -1:
        #         # means it's a break
        #         return -1
        #     res += 1
        #     i = i - (len(target) - ans) + 1
        #     print ' aab i bacha ', i
        #     # i = i - ans
        # return res

print Solution().shortestWay('xyz', 'xzyxz')





















