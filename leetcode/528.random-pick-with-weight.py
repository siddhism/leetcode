#
# @lc app=leetcode id=528 lang=python
#
# [528] Random Pick with Weight
#
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        if not w:
            return
        self.n = len(w)
        self.s = sum(w)
        for i in range(1, self.n):
            self.w[i] = self.w[i] + self.w[i-1]
        

    def pickIndex(self):
        """
        :rtype: int
        """
        # pick element at index i from self.cum
        # since it's cummulative [1,3,4,4] => 1,4,8,12. find counter index bisect right
        import random
        seed = random.randint(1,self.s)
        lo, hi = 0, self.n - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if seed <= self.w[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

