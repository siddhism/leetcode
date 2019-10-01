#
# @lc app=leetcode id=298 lang=python
#
# [298] Binary Tree Longest Consequtive Sequence
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, node, count, parent_val):
        if not node:
            return 

        # if this node is in consecutive sequence
        if node.val == parent_val + 1:
            count = count + 1
            # set answer
            self.ans = max(count, self.ans)
        else:
            # reset count at this parent
            count = 1

        self.traverse(node.left, count, node.val)
        self.traverse(node.right, count, node.val)

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # first we'll traverse traverse and find longest conseq
        if not root:
            return 0

        self.result = []
        count = 0
        self.ans = 1
        # root 's count will start from 1 due to traverse logic
        self.traverse(root, count, root.val)
        return self.ans
                


        