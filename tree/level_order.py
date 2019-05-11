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


def preorder(node):
    if not node:
        return

    print node.data
    preorder(node.left)
    preorder(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)



def level_order(root):
    node = root
    queue = []
    queue.append(node)
    while len(queue) > 0:
        node = queue[0]
        queue = queue[1:]
        print (node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

level_order(root)

