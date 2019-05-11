class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


def get_depth(node):
    d = 0
    while node:
        node = node.left
        d += 1
    return d

def is_leaf(node):
    if not node.left and not node.right:
        return True
    return False

def is_perfect_tree(node, d, level=0):
    if not node:
        return True

    if is_leaf(node):
        return d == level + 1

    if not node.left or not node.right:
        return False

    is_perfect = is_perfect_tree(node.left, d, level+ 1) and \
            is_perfect_tree(node.right, d, level+1)
    return is_perfect



inorder(root)
print ('\n')
d = get_depth(root)
is_perfect = is_perfect_tree(root, d, level=0)
print ('is perfect tree ', is_perfect)
