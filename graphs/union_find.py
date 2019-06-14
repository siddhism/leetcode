n = 10
parent = [i for i in range(n + 1)]
size = [1 for i in range(n + 1)]

def union(a, b, parent, size):
    pass


def find(a, b, parent):
    pass

def root(i, parent):
    while i != parent[i]:
        i = parent[i]
    return i


union(0, 1)
union(1, 2)
union(4, 5)
union(0, 1)
union(0, 1)
