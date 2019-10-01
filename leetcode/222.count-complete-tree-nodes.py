#
# @lc app=leetcode id=222 lang=python
#
# [222] Count Complete Tree Nodes
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_depth(node):
        if not node:
            return
        self.depth += 1
        self.get_depth(node.left)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.depth = 0
        self.get_depth(root)
        print 'depth ', self.depth
        
        # do level order traversal till n-1 level and exit as early as possible
        # traverse to n - 1 left tree

