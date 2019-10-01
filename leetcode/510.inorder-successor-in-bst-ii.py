#
# @lc app=leetcode id=510 lang=python
#
# [510] Inorder successer in BST
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        # inorder traversal
        stack = []
        prev_node = node.parent
        root = node # start from given node
        # go to it's parent till you have greater value
        while node.parent:
            if node.parent.val > node.val:
                return node.parent
            node = node.parent
        
        return None


        