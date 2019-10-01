#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            # print (root.val)
            k = k - 1 # inorder k'th element
            root = stack.pop()
            if k == 0:
                return root.val
            root = root.right
        
        return None       

