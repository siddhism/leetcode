# Python 3 program to find LCA in a
# tree represented as parent array.

# Function to find the Lowest
# common ancestor
def findLCA(n1, n2, parent):
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
    visited[i] = False


# Maximum capacity of binary tree
parent = {}
visited = {}

# Root marked
parent[20] = -1
visited[20] = False
insertAdj(parent, 8, 20)
insertAdj(parent, 22, 20)
insertAdj(parent, 4, 8)
insertAdj(parent, 12, 8)
insertAdj(parent, 10, 12)
insertAdj(parent, 14, 12)

print(findLCA(10, 14, parent))

# This code is contributed by
    