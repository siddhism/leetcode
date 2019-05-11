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


root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(2)


def calculate_sum(node):
    if not node:
        return 0 # return true for leaf nodes
    # Sum the left and right nodes whichever is available
    sum = node.data + calculate_sum(node.left) + calculate_sum(node.right)
    print (node.data, sum)
    return sum

inorder(root)
print ('\n')
data = calculate_sum(root)
print (data)
