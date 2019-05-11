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


def construct():
    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(1)
    root.left.right.left = Node(1)
    root.right = Node(-1)
    root.right.left = Node(4)
    root.right.left.left = Node(1)
    root.right.left.right = Node(2)
    root.right.right = Node(5)
    root.right.right.right = Node(2)
    return root


def get_k_sum_elements(node, k):
    """
    get elements in the tree whose sum is k,
    starting from any node and ending at any node
    """
    paths = []
    if not node:
        return paths
    # start a path from self node always
    self_result = (node.data, [node.data])
    if node.data == k:
        # condition when this node itself is equal to k
        print [node.data]
    paths.append(self_result)

    left_paths = get_k_sum_elements(node.left, k)
    right_paths = get_k_sum_elements(node.right, k)
    current_data = node.data
    for (sum_left, l_path) in left_paths:
        new_sum = sum_left + current_data
        l_path.append(current_data)
        result = (new_sum, l_path)
        paths.append(result)
        if new_sum == k:
            print (l_path)

    for (sum_right, r_path) in right_paths:
        new_sum = sum_right + current_data
        r_path.append(current_data)
        result = (new_sum, r_path)
        paths.append(result)
        if new_sum == k:
            print (r_path)

    # print (' For node ', node, ' Returing paths ', paths)
    return paths

root = construct()
k = 5
get_k_sum_elements(root, k)
