#
# @lc app=leetcode id=701 lang=python
#
# [701] Insert into a Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)

        def dfs(node, val):
            if not node:
                return None

            if not node.left and val < node.val:
                # it's a leaf node, attach value here
                node.left = TreeNode(val)
            if not node.right and val > node.val:
                node.right = TreeNode(val)
            
            if val < node.val:
                dfs(node.left, val)
            else:
                dfs(node.right, val)

        dfs(root, val)
        return root




