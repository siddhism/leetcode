n = 10
parent = [i for i in range(n + 1)]
size = [1 for i in range(n + 1)]

def union(a, b, parent, size):
    parent_a = root(a)
    parent_b = root(b)
    if size[parent_b] < size[parent_a]:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


def find(a, b, parent):
    if root(a) == root(b):
        return True
    return False

def root(i, parent):
    while i != parent[i]:
        i = parent[i]
    return i


union(0, 1)
union(1, 2)
union(4, 5)
union(0, 1)
union(0, 1)
