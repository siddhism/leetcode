class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def inorder(node):
    if not node:
        return

    inorder(node.left)
    print node.data
    inorder(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


def is_leaf(node):
    if not node.left and not node.right:
        return True
    return False

def is_full_binary(node):
    if not node:
        return True

    if is_leaf(node):
        return True

    if not node.left or not node.right:
        return False

    cond = is_full_binary(node.left) and is_full_binary(node.right)
    # print ('Returning ', cond, ' for node ', node)
    return cond



inorder(root)
print ('\n')
is_full_binary_tree = is_full_binary(root)
print ('is full binary tree ', is_full_binary_tree)
