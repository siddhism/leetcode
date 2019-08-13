# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def is_valid_subtree(self, node, min_val, max_val):
        # print 'called for node ', node.val , 'with' , ' : ', min_val, max_val
        if not node:
            return True
        is_valid = min_val < node.val < max_val
        if not is_valid:
            return False
        is_left = self.is_valid_subtree(node.left, min_val, node.val)
        is_right = self.is_valid_subtree(node.right, node.val, max_val)
        return is_left and is_right
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        if not root:
            return True
        is_left = self.is_valid_subtree(root.left, -sys.maxint, root.val)
        is_right = self.is_valid_subtree(root.right, root.val, sys.maxint)
        return is_left and is_right
