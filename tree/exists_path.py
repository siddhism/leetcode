# this is coded after checking solution
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


def is_leaf(node):
    if not node.left and not node.right:
        return True
    return False


def exists_path(root, arr, n, index):
    """
    checks if arr[index] exists at current node
    """
    print (' in exist path function ', root, arr, index)
    if root is None:
        # If this is last node, check if we have completed looking into array
        return n == index + 1
    if not root.left and not root.right:
        # If node is leaf node, check if it's last in sequence and matches with data
        return (index == n and arr[index] == root.data)
    if index < n:
        element = arr[index]
        if root.data == element:
            check_left = exists_path(root.left, arr, n, index+1)
            check_right = exists_path(root.right, arr, n, index+1)
            return check_left or check_right
        else:
            return False


arr = [5, 8, 6, 7]
n = len(arr)  
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.left.left = Node(1)
root.right.left = Node(6)
root.right.left.right = Node(7) 
if exists_path(root, arr, n, 0):
    print 'Exists in the given tree'
else:
    print 'Does not exist in given tree'
