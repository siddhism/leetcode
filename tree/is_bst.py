# A binary tree node
import sys


class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_bst(node, min_limit, max_limit):
    if not node:
        return True
    if not (min_limit < node.data < max_limit):
        return False
    l_path = is_bst(node.left, min_limit, node.data)
    r_path = is_bst(node.right, node.data, max_limit)
    return l_path and r_path


# Driver program to test above function
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
if (is_bst(root, -sys.maxint, sys.maxint)):
    print "Is BST"
else:
    print "Not a BST"
