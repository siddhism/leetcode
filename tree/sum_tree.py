class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(node):
    if not node:
        return

    inorder(node.left)
    print node.data,
    inorder(node.right)


root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.left = Node(3)


def get_sum(node):
    if not node:
        # left node
        return True, 0
    left_is_sum, left_sum = get_sum(node.left)[0], get_sum(node.left)[1] 
    right_is_sum, right_sum = get_sum(node.right)[0], get_sum(node.left)[1]
    current_sum = left_sum + right_sum
    if left_is_sum and right_is_sum:
        return True, current_sum
    else:
        return False, current_sum

inorder(root)
is_sum, total = get_sum(root)
print (is_sum, total)
