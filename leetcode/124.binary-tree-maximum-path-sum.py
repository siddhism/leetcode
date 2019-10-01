# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        result = set()
        def inorder(node):
            if not node:
                return 0
            L = inorder(node.left)
            R = inorder(node.right)
            print 'vals ', L+node.val, R+node.val, L+R+node.val, 0+node.val
            cur_max = max(L, R, L+R, 0) + node.val
            result.add(cur_max)
            for_parent = max(L, R, 0) + node.val
            result.add(for_parent)
            return for_parent

        at_root = inorder(root)
        print result
        result.add(at_root)
        return max(result)
        
        
            
            