#
# @lc app=leetcode id=700 lang=python
#
# [700] Search in a Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def dfs(node, val):
            if not node:
                return None
            if node.val == val:
                return node
            
            elif val < node.val :
                return dfs(node.left, val)
            else:
                return dfs(node.right, val)

        return dfs(root, val)

