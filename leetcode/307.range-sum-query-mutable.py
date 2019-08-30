#
# @lc app=leetcode id=307 lang=python
#
# [307] Range Sum Query - Immutable
#
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.array = [0] * n
        self.tree = [0] * (n + 1)
        for i in range(n):
            self.update(i, nums[i])
        
    def get_next(self, index):
        return index + (index & -index)
    
    def get_parent(self, index):
        return index - (index & -index)

    def update(self, index, val):
        current = self.array[index]
        self.array[index] = val
        diff = self.array[index] - current
        index += 1
        while index <= len(self.array):
            self.tree[index] += diff
            index = self.get_next(index)
        
    def prefix_sum(self, index):
        total = 0
        index += 1
        while index > 0:
            total += self.tree[index]
            index = self.get_parent(index)
        return total

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        a = self.prefix_sum(i-1)
        b = self.prefix_sum(j)
        # print 'i ', i, ' j ', j , ' a ', a, ' b ', b, ' diff ', a - b
        return (b - a)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

