#
# @lc app=leetcode id=257 lang=python
#
# [257] Binary Tree Paths
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_path(self, node, path):
        path = path[:]
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            # print 'returning ' , [path]
            self.paths.append(path)
        else:
            self.get_path(node.left, path)
            self.get_path(node.right, path)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.paths = []
        self.get_path(root, path=[])
        out = ['->'.join(map(str, arr)) for arr in self.paths]
        return out
        

