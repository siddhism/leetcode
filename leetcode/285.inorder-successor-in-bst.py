#
# @lc app=leetcode id=285 lang=python
#
# [285] Inorder successer in BST
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        # inorder traversal
        stack = []
        prev_node_val = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if prev_node_val == p.val:
                return root
            prev_node_val = root.val

            root = root.right
        
        return None


        