class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
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

def is_leaf(node):
    if not node.left and not node.right:
        return True
    return False

def print_left_leaves(node, is_left=True):
    """
    prints only left leaves for a tree
    node: node of a tree
    is_left : default true for root node
    """
    global sum
    if not node:
        return # do nothing if for any leave it's called for their child

    if is_leaf(node) and is_left:
        sum = sum + node.data

    print_left_leaves(node.left, is_left=True)
    print_left_leaves(node.right, is_left=False)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)




inorder(root)
print ('\n')
sum = 0
print_left_leaves(root)
print 'sum ', sum