class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

def construct():
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.left = Node(6) 
    root.right.right = Node(7)
    return root


def is_leaf(node):
    if not node.left and not node.right:
        return True
    return False

def find_path(current, path, key):
    if not current:
        return False
    print ('Node ', current, ' path ', path)
    path.append(current.data)
    if current.data == key:
        return True
    found_left = False
    found_right = False
    if current.left:
        found_left = find_path(current.left, path, key)
    if current.right:
        found_right = find_path(current.right, path, key)
    if found_left or found_right:
        return True
    path.pop()
    return False


def find_lca(root, n1, n2):
    path1 = []
    path2 = []
    find_path(root, path1, n1)
    find_path(root, path2, n2)
    print path1, path2
    if not path1 or not path2:
        return None # Not found
    # compare paths to get first different value and return value before it
    i = 0
    while i < len(path1) and i < len(path2):
        a = path1[i]
        b = path2[i]
        if a != b:
            break
        i = i + 1
    return path1[i-1]




root = construct()


print "LCA(4, 5) = ", find_lca(root, 4, 5)
print "LCA(4, 6) = ", find_lca(root, 4, 6)
print "LCA(3, 4) = ", find_lca(root, 3, 4) 
print "LCA(2, 4) = ", find_lca(root,2, 4) 
