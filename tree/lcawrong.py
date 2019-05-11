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

def find_path(current, key, path=[]):
    """Find path of node from current"""
    """
    This is wrong code 
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        xxxxxx                xxxxxx
            xxxxxxx     xxxxxx
                xxxxxxxxxxxx
                xxxxxxxxxxxx
            xxxxxx      xxxxxx
        xxxxxx                xxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    """
    if not current:
        return False, path
    # print ('Called for node ', current, ' with path ', path)
    path.append(current.data)
    if is_leaf(current):
        if current.data == key:
            return True, path
        return False, []

    # if does not match, go left and append path
    found_left = False
    found_right = False
    if current.left:
        found_left, left_path = find_path(current.left, key, path)
        if found_left:
            return True, left_path
    if current.right:
        found_right, right_path = find_path(current.right, key, path)
        if found_right:
            return True, right_path
    path.pop()
    return False, []


def find_lca(root, n1, n2):
    path1 = find_path(root, n1, path=[])[1]
    path2 = find_path(root, n2, path=[])[1]
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
