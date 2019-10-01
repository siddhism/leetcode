#
# @lc app=leetcode id=235 lang=python
#
# [235] Lowest Common Ancestor of a Binary Search Tree
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
        orig_p, orig_q = p, q
        p = min(orig_p, orig_q)
        q = max(orig_p, orig_q)
        self.dfs(root, p, q)
        return self.lca
    
    def dfs(self, root, p, q):
        print (root.val, p, q, self.lca.val)
        if not root:
            return
        if p < root.val < q or p <= root.val < q or p < root.val <= q:
            self.lca = TreeNode(root.val)
        elif root.val > p and root.val > q:
            self.dfs(root.left, p, q)
        elif root.val < p and root.val < q:
            self.dfs(root.right, p, q)



