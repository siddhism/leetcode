#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#
class Solution(object):

    def is_cyclic(self, node, visited, rec_stack, path=[]):
        visited[node] = True
        rec_stack[node] = True

        # traverse neighbours which are 
        for nxt in self.graph[node]:
            if not visited[nxt]:
                child_is_cyclic = self.is_cyclic(nxt, visited, rec_stack, path)
                if child_is_cyclic:
                    return True
            elif rec_stack[nxt]:
                return True

        # mark in rec_stack once all childs are traversed. after all dependancy
        rec_stack[node] = False
        path.append(node)
        # if everything got processed return false - not cyclic
        return False

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not numCourses:
            return []

        self.V = numCourses
        from collections import defaultdict
        self.graph = defaultdict(list)

        for k,v in prerequisites:
            # store in rev order and do topological sort to take courses to take first
            self.graph[k].append(v)
        
        print self.graph

        visited = [False for _ in range(self.V)]
        answer = []
        path = []

        for node, _ in self.graph.items():
            if not visited[node]:
                rec_stack = [False for _ in range(self.V)]
                cycle = self.is_cyclic(node, visited, rec_stack, path)
                if cycle:
                    return []

        for node in range(self.V):
            if not visited[node]:
                path.append(node)

        return path


# print Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
# print Solution().findOrder(2, [[0,1]])
# print Solution().findOrder(2, [[1,0]])
# print Solution().findOrder(3, [[1,0]])
# print Solution().findOrder(1, []) == [0]
# print Solution().findOrder(3, [[2,0],[2,1]])





