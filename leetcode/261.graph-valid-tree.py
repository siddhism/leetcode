#
# @lc app=leetcode id=261 lang=python
#
# [261] Graph Valid Tree
#
class Solution(object):

    def is_cyclic(self, node, visited, parent):
        visited[node] = True

        for nxt in self.graph[node]:
            if not visited[nxt]:
                cyclic = self.is_cyclic(nxt, visited, node)
                if cyclic:
                    return True
            # if it is visited and not the parent from which it came, it's a cycle
            elif nxt != parent:
                return True

        return False

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        self.graph = defaultdict(list)

        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        visited = [False for _ in range(n)]

        # start DFS from any node
        cyclic = self.is_cyclic(0, visited, -1)
        # print 'edges ', edges, 
        # print 'visited ', visited, 
        # print 'cylic', cyclic
        if cyclic:
            # means not a valid tree
            return False
        for i in range(n): 
            if not visited[i]: 
                return False
        # if none of the path result in cycle it's a valid tree
        return True

# print Solution().validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]) == False
# print Solution().validTree(5, [[0,1], [0,2], [0,3], [1,4]]) == True
# print Solution().validTree(4, [[0,1],[2,3]]) == False
# print Solution().validTree(2, [[1,0]]) == True

