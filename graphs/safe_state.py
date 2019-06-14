from collections import defaultdict

class Graph:

    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V
        self.white, self.gray, self.black = 0, 1, 2

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        for k, v in self.graph.items():
            print k, ' - > ', v

    def dfs_util(self, node, color):

        if color[node] != self.white:
            # if node being visited is not white, means it should be black (other)
            return color[node] == self.black
        # if color[node] == self.gray:
        #     return False
        # if color[node] == self.black:
        #     return True
        color[node] = self.gray
        # explore all neighbours
        for nei in self.graph[node]:
            if color[nei] == self.black:
                continue
            if color[nei] == self.gray or not(self.dfs_util(nei, color)):
                # either it's gray or dfs for child returns false
                return False
        # once all childs are explored, set it to black
        color[node] = self.black
        return True

    def dfs(self, node):
        # Initialize all node as white, as defaultdict will initialize to 0
        color = defaultdict(int)
        return self.dfs_util(node, color)

    # def is_cycle_util(self, node, visited, rec_stack):
    #     visited[node] = True
    #     rec_stack[node] = True
    #     print node, 
    #     # Traverse dfs
    #     for v in self.graph[node]:
    #         if not visited[v]:
    #             if self.is_cycle_util(v, visited, rec_stack):
    #                 return True
    #         if visited[v] and rec_stack[v]:
    #             # cycle found
    #             return True
    #     # All childs traversed, remove current node from recursive stack and return false
    #     rec_stack[node] = False
    #     return False


class Solution(object):


    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        V = len(graph)
        g = Graph(V)
        for node_index, dests in enumerate(graph):
            for dest in dests:
                g.add_edge(node_index, dest)
        # g.print_graph()
        results = []
        for v in range(V):
            if g.dfs(v):
                results.append(v)
        return results



inpt = [[1,2],[2,3],[5],[0],[5],[],[]]

output = Solution().eventualSafeNodes(inpt)
print output