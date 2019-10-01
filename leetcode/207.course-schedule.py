#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#
class Solution(object):

    def is_cyclic(self, node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        # traverse neighbours which are 
        for nxt in self.graph[node]:
            if not visited[nxt]:
                child_is_cyclic = self.is_cyclic(nxt, visited, rec_stack)
                if child_is_cyclic:
                    return True
            elif rec_stack[nxt]:
                return True

        # mark in rec_stack once all childs are traversed. after all dependancy
        rec_stack[node] = False
        # if everything got processed return false - not cyclic
        return False


    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        self.graph = defaultdict(list)
        if not prerequisites:
            return True

        self.V = numCourses
        # build graph
        for item in prerequisites:
            self.graph[item[0]].append(item[1])
        print self.graph

        visited = [False for _ in range(self.V)]

        for node in range(self.V):
            if not visited[node]:
                rec_stack = [False for _ in range(self.V)]
                result = self.is_cyclic(node, visited, rec_stack)
                if result:
                    return False
        # we have to return the result as opposite of cyclic
        return True

# print Solution().canFinish(2, [[1,0]]) == True
# print Solution().canFinish(2, [[1,0], [0,1]]) == False
# print Solution().canFinish(3, [[1,0],[2,0]]) == True
# print Solution().canFinish(3, [[0,1],[0,2],[1,2]]) == True
        
