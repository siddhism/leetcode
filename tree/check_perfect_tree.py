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


def get_height(node):
    if not node:
        return 0
    lheight = get_height(node.left)
    rheight = get_height(node.right)
    if lheight >= rheight:
        cur_height = lheight
    else:
        cur_height = rheight
    cur_height = cur_height + 1
    # or above can be written as cur_height = max(lheight, rheight) + 1
    return cur_height

def is_leaf(node):
    if not node.left and not node.right:
        return True
    return False

def is_perfect_tree(node):
    if is_leaf(node):
        return True
    l_height = get_height(node.left)
    r_height = get_height(node.right)
    cond1 = l_height == r_height
    cond2 = node.left and node.right
    if cond1 and cond2:
        return is_perfect_tree(node.left) and is_perfect_tree(node.right)
    else:
        return False



inorder(root)
print ('\n')
data = is_perfect_tree(root)
print ('is perfect tree ', data)
