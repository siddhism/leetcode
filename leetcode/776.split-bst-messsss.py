#
# @lc app=leetcode id=776 lang=python
#
# [776] Split BST
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def find_split_point(self, node, is_left_path, V):
        """find the split point where both trees will be separated"""
        if not node:
            return
        
        if node.val == V:
            # means we have found the point where we have to split
            if is_left_path:
                self.t2 = node
            else:
                self.t2 = node.right

        # while going left if we find val greater then V, it's pivot
        if is_left_path and node.val < V:
            self.t2 = node # t1 was already set by parent
        # while going right if we find val greater then V, it's pivot
        if not is_left_path and node.val > V:
            self.t2 = node

        if V < node.val:
            # find in left tree, root is split, current parent is split point
            self.t1 = node
            self.find_split_point(node.left, True, V)
        else:
            self.t1 = node
            self.find_split_point(node.right, False, V)




    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        # we do two traversal, one to find the t1, t2 root
        # then to construct the given trees
        if not root:
            # change as per expected in blank case
            return [TreeNode(None), TreeNode(None)]
        self.root = root
        self.t1 = root # by default root is first pivot point
        self.t2 = None
        # if root itself is pivot
        if root.val == V:
            self.t1 = root
            self.t2 = root.right
            return [self.t1, self.t2]
        else:
            self.find_split_point(root.left, True, V)
            self.find_split_point(root.right, False, V)
        print (self.t1, self.t2)

        # construct tree
        bst_t1 = BST(self.t1)
        bst_t2 = BST(self.t2)

        def construct_t1(node, t1):
            if not node or not t1:
                return
            if node.val <= t1.val:
                new_node = TreeNode(node.val)
                bst_t1.insert(bst_t1.root, node.val)
                
        def construct_t2(node, t2):
            if not node or not t2:
                return
            if node.val <= t2.val:
                new_node = TreeNode(node.val)
                bst_t2.insert(bst_t2.root, node.val)
                
        construct_t1(root, self.t1)
        construct_t2(root, self.t2)
        return [self.t1, self.t2]


class BST(object):

    def __init__(self, root):
        self.root = root
    
    def insert(self, node, val, is_left=False):
        if not node:
            new_node = TreeNode(val)
            return new_node
                
        if val < node.val:
            L = self.insert(node.left, val)
            if L:
                node.left = L
        else:
            R = self.insert(node.right, val)
            if R:
                node.right = R
    

        