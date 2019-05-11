# Python 3 program to find LCA in a
# tree represented as parent array.

# Maximum value in a node
MAX = 1000

# Function to find the Lowest
# common ancestor
def findLCA(n1, n2, parent):

    # Create a visited vector and mark
    # all nodes as not visited.
    visited = [False for i in range(MAX)]

    visited[n1] = True

    # Moving from n1 node till root and
    # mark every accessed node as visited
    while (parent[n1] != -1):
        visited[n1] = True
        # Move to the parent of node n1
        n1 = parent[n1]

    # For second node finding the
    # first node common
    while (visited[n2] == False):
        n2 = parent[n2]

    return n2

# Insert function for Binary tree
def insertAdj(parent, i, j):
    parent[i] = j


# Maximum capacity of binary tree
parent = [0 for i in range(MAX)]

# Root marked
parent[20] = -1
insertAdj(parent, 8, 20)
insertAdj(parent, 22, 20)
insertAdj(parent, 4, 8)
insertAdj(parent, 12, 8)
insertAdj(parent, 10, 12)
insertAdj(parent, 14, 12)

print(findLCA(10, 14, parent))

# This code is contributed by
