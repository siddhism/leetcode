#
# @lc app=leetcode id=951 lang=python
#
# [951] Flip Equivalent Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def is_leaf(self, node):
        if not node.left and not node.right:
            return True
        return False

    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        # if not root1 and not root2:
        #     return True
        # if (root1 and self.is_leaf(root1)) or (root2 and self.is_leaf(root2)):
        #     return False
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            # any one of them is none or vals are unequal. immediate break
            return False

        a1 = self.flipEquiv(root1.left, root2.left)
        a2 = self.flipEquiv(root1.right, root2.right)
        a3 = self.flipEquiv(root1.left, root2.right)
        a4 = self.flipEquiv(root1.right, root2.left)
        # print ('At ', root1.val, root2.val, (a1, a2, a3, a4), ' vals equal ', a5)
        res = (a1 and a2 or a3 and a4)
        # print ('result ', res)
        return res
        
# @lc code=end

# test case [0,3,1,null,null,null,2]\n[0,3,1,2]
# last test case which failed
# [0,1,4,2,null,7,null,3,6,null,null,5]\n[0,4,1,7]
