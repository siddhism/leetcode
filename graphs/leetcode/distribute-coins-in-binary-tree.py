# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, total):
            if not root:
                return
            if root.left:
                root_need = 1 - root.val
                if root_need:
                    total += root_need
                    root.left.val = root.left.val - root_need
                    root.val = 1
                dfs(root.left, total)
            if root.right:
                root_need = 1 - root.val
                if root_need:
                    total += root_need
                    root.right.val = root.right.val - root_need
                    root.val = 1
                dfs(root.right, total)
        total = 0
        dfs(root)
        return total
