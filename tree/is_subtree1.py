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


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


def is_leaf(node):
    if not node.left and not node.right:
        return True
    return False


inorder(root)
print ('\n')

def are_identical(root1, root2):
    """
    checks if trees rooted at root1 & root2 are same
    """

    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False

    cond = root1.data == root2.data and are_identical(root1.left, root2.left) \
            and are_identical(root1.right, root2.right)
    return cond


def is_subtree(t, sub):
    """Check if sub is a subtree of t
    """
    if not sub:
        return True # since None is always a subtree of any tree
    if not t:
        return False

    if are_identical(sub, t):
        return True

    # check if any of left or right subtree of t is equivalent to sub
    return is_subtree(t.left, sub) or is_subtree(t.right, sub)

# Driver program : courtesy geeks for geeks

""" TREE 1 
     Construct the following tree 
              26 
            /   \ 
          10     3 
        /    \     \ 
      4      6      3 
       \ 
        30 
    """
  
T = Node(26) 
T.right = Node(3) 
T.right.right  = Node(3) 
T.left = Node(10) 
T.left.left = Node(4) 
T.left.left.right = Node(30) 
T.left.right = Node(6) 
  
""" TREE 2 
     Construct the following tree 
          10 
        /    \ 
      4      6 
       \ 
        30 
    """
S = Node(10) 
S.right = Node(6) 
S.left = Node(4) 
S.left.right = Node(30) 
  
if is_subtree(T, S): 
    print "Tree 2 is subtree of Tree 1"
else : 
    print "Tree 2 is not a subtree of Tree 1"
  