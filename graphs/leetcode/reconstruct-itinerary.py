
class Graph:
    def __init__(self, v):
        from collections import defaultdict
        self.v = v
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited, order):
        order.append(v)
        for dest in sorted(self.graph[v]):
            if not visited[v][dest]:
                visited[v][dest]= True
                self.dfs_util(dest, visited, order)

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        n = len(tickets)
        g = Graph(n)
        # really helpful thing i thought off
        visited = defaultdict(dict)

        for ticket in tickets:
            src = ticket[0]
            dest = ticket[1]
            g.add_edge(src, dest)
            visited[src][dest] = False
        order = []
        g.dfs_util('JFK', visited, order)
        return order

print Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
print Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])

