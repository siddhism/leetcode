#
# @lc app=leetcode id=112 lang=python
#
# [112] Path Sum
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def is_leaf_node(self, node):
        if not node.left and not node.right:
            return True
        return False

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if self.is_leaf_node(root):
            return root.val == sum
        # pass along to the same function with remaining sum to come up
        l_path = self.hasPathSum(root.left, sum-root.val)
        r_path = self.hasPathSum(root.right, sum-root.val)
        # if any of left or right subtree returns true, it means such path exists
        return l_path or r_path
        

