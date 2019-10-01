#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def depth(node):
            if not node:
                # no node, parent has to take decision
                return 0, True
            ld, l_res = depth(node.left)
            rd, r_res = depth(node.right)
            # if depth diff is > 1 or one of l/r returned false
            # print (' node ', node.val, ' ld ', ld, ' rd', rd,  ' returning ', max(ld, rd) + 1)
            if abs(ld - rd) > 1 or not (l_res and r_res):
                return max(ld, rd) + 1, False
            return max(ld, rd) + 1, True
        
        d, res = depth(root)
        return res

