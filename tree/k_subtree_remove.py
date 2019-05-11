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
    print node.data,
    inorder(node.right)


def construct():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(12)
    root.right.right.left = Node(10)
    root.right.right.left.right = Node(11)
    root.left.left.right.left = Node(13)
    root.left.left.right.right = Node(14)
    root.left.left.right.right.left = Node(15)
    return root


def is_leaf(node):
    if not node.left and not node.right:
        return True


def subtree_sum(node, total, k):
    if not node:
        return False
    
    if is_leaf(node):
        # if total is greater than k then we will keep this leaf
        return (total >= k)

    keep_left = False
    keep_right = False
    if node.left:
        keep_left = subtree_sum(node.left, total + node.left.data, k)
    if node.right:
        keep_right = subtree_sum(node.right, total + node.right.data, k)

    if not keep_left:
        node.left = None
    if not keep_right:
        node.right = None
    return keep_left or keep_right



root = construct()
k = 45
inorder(root)
print('\n')
subtree_sum(root, total=root.data, k=k)
print('\n')
inorder(root)
print('\n')
