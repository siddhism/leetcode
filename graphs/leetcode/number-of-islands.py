from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 

class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # created a key using u,v
        self.graph[u].append(v)

    def print_graph(self):
        for node, adj in self.graph.items():
            print node, ' -> ', adj

    def dfs_util(self, v, visited):
        visited[v] = True
        # print v,
        for node in self.graph[v]:
            if not visited[node]:
                self.dfs_util(node, visited)


class Solution(object):

    def dfs(self, key, visited):
        visited[key] = True
        # print 'key ', key
        for item in self.graph_obj.graph[key]:
            if not visited[item]:
                self.dfs(item, visited)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        self.graph_obj = Graph(n)
        for i in range(n):
            for j in range(m):
                if not int(grid[i][j]):
                    continue
                current = [i, j]
                current_key = i*m + j
                if i-1>=0 and int(grid[i-1][j]):
                    left = [i-1, j]
                    key = (i-1) * m + j
                    self.graph_obj.add_edge(key, current_key)
                if i+1<n and int(grid[i+1][j]):
                    right = [i+1, j]
                    key = (i+1) * m + j
                    # print right, current
                    self.graph_obj.add_edge(key, current_key)
                if j-1>=0 and int(grid[i][j-1]):
                    bottom = [i, j-1]
                    key = (i) * m + (j - 1)
                    self.graph_obj.add_edge(key, current_key)
                if j+1 < m and int(grid[i][j+1]):
                    top = [i, j+1]
                    key = (i) * m + (j + 1)
                    self.graph_obj.add_edge(key, current_key)
        # self.graph_obj.print_graph()
        # print self.graph_obj.graph

        count = 0
        visited = [False for _ in range(m*n)]
        for i in range(n):
            for j in range(m):
                key = i * m + j
                if not visited[key] and int(grid[i][j]):
                    # print 'calling dfs for ', i, j, ' key ', key
                    self.dfs(key, visited)
                    count += 1
        return count

# print Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print Solution().numIslands([['1', '1','0','0','0'],['1', '1','0','0','0'],['0','0','1','0','0'],['0','0','0','1', '1']])

