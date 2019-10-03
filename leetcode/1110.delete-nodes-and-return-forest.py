#
# @lc app=leetcode id=1110 lang=python
#
# [1110] Delete Nodes And Return Forest
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        # dsu = DSU(1001)
        forest = set()
        # to detach should contain list of node and left=True, right=True to detach childs
        to_detach = []
        to_delete = dict({item: True for item in to_delete})

        # traverse and create list of childs which needs to be detached
        # new roots which get created are also added to forest already
        def inorder(node, is_root=False):
            if not node:
                return
            # TODO : handle case when the to_delete node is already in forest?? : uniqueness already given
            if to_delete.get(node.val):
                if node.left and not to_delete.get(node.left.val):
                    # to be part of forest, this one shouldn't be deletable
                    forest.add(node.left)
                if node.right and not to_delete.get(node.right.val):
                    forest.add(node.right)

            if node.left and to_delete.get(node.left.val):
                to_detach.append((node, True, False))
            if node.right and to_delete.get(node.right.val):
                to_detach.append((node, False, True))

            inorder(node.left)
            # print (node.val)
            inorder(node.right)

        inorder(root, is_root=True)
        print ('forest already prepared ', [node.val for node in forest])
        print (' to detach list ', [(node[0].val, node[1], node[2]) for node in to_detach])
        # second round, go through to_detach, detach and add roots to forest
        for node, delete_left, delete_right in to_detach:
            if delete_left:
                node.left = None
            if delete_right:
                node.right = None
            if node == root and not to_delete.get(root.val):
                forest.add(node)

        if root.val not in to_delete:
            forest.add(root)

        return list(forest)
        
# @lc code=end
# Test case  = [1,2,4,null,3]\n[3]
# test case 2 = [1,2,3,null,null,null,4]\n[2,1]
