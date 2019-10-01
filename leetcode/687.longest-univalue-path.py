#
# @lc app=leetcode id=687 lang=python
#
# [687] Longest Univalue Path
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, root):
        if not root:
            return 0
        left_length = self.traverse(root.left)
        right_length = self.traverse(root.right)
        left_arrow = 0
        right_arrow = 0
        if root.left and root.left.val == root.val:
            left_arrow = left_length + 1
        if root.right and root.right.val == root.val:
            right_arrow = right_length + 1

        self.cur_max = max(self.cur_max, left_arrow + right_arrow)
        return max(left_arrow, right_arrow)

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        count = 0
        self.cur_max = 0
        result = self.traverse(root)
        print (count, self.cur_max)
        # now the problem reduces to find length of longest common elements
        return self.cur_max














