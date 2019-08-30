#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []
        from collections import defaultdict
        lot = defaultdict(list)
        queue.append((root, 0))
        # lot[0].append(root.val)
        while queue:
            top, level = queue.pop(0)
            lot[level].append(top.val)
            if top.left:
                queue.append((top.left, level+1))
            if top.right:
                queue.append((top.right, level+1))
        return lot.values()

        

