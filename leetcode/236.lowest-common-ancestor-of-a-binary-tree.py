#
# @lc app=leetcode id=236 lang=python
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.lca = None
        self.dfs(root)
        return self.lca
    
    def dfs(self, root, value):
        if not root:
            return False
        
        found_l = self.dfs(root.left, value)
        found_r = self.dfs(root.right, value)
        mid = root.val == p.val or root.val == q.val

        # If any two of the three flags left, right or mid become True.
        if mid + found_l + found_r >= 2:
            return True

        return (mid or found_l or found_r)

        

        

class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans