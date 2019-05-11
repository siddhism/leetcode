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


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(2)


def is_sum_tree(node):
    if not node:
        return True # return true for leaf nodes
    # Sum the left and right nodes whichever is available
    child_sum = is_sum_tree(node.left) and is_sum_tree(node.right)
    # if both and left child are not there, return child value
    # since nothing is there to add
    if not node.left and not node.right:
        return child_sum
    total = 0
    if node.left:
        total += node.left.data
    if node.right:
        total += node.right.data
    self_sum = total == node.data
    sum_tree_at_current_node = child_sum and self_sum
    print (node.data, sum_tree_at_current_node)
    return sum_tree_at_current_node

inorder(root)
data = is_sum_tree(root)
print (data)
