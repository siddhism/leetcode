import sys
from collections import defaultdict


class Graph:

    def __init__(self, V):
        self.V = V + 1
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def print_solution(self, dist):
        for i in range(self.V):
            print i, 't ', dist[i]

    def min_distance(self, dist, spt_set):
        min_dist = sys.maxint
        min_index = -1
        for v in range(1, self.V):
            if dist[v] < min_dist and not spt_set[v]:
                min_dist = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxint] * (self.V)
        dist[src] = 0
        spt_set = [False] * self.V
        # dist[src] = 0
        # self.spt_set[src] = True

        for _ in range(self.V):
            # Get the node at minimum distance from source
            u = self.min_distance(dist, spt_set)
            # mark this in spt set
            spt_set[u] = True

            # update all the near by nodes distance if they are not already visited
            # and they can be reached via this node for achieving shortest path
            for nei, d in self.graph[u]:
                if not spt_set[nei] and dist[nei] > dist[u] + d:
                    dist[nei] = dist[u] + d
        self.print_solution(dist)
        return dist


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        g = Graph(N)
        for item in times:
            u, v, w = item
            g.add_edge(u, v, w)
        dist = g.dijkstra(K)
        if sys.maxint in dist[1:]:
            return -1
        else:
            return max(dist[1:])


# times = [[2,1,1],[2,3,1],[3,4,1]]
# N = 4
# K = 2
# times = [[2,1,1],[2,3,1],[3,4,1]]
# N = 4
# K = 2
times = [[3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85], [5, 2, 22], [2, 4, 23], [1, 4, 43], [4, 5, 75], [5, 1, 15], [
    1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22], [5, 4, 31], [1, 2, 0], [2, 5, 4], [4, 2, 51], [3, 1, 36], [2, 3, 59]]
N = 5
K = 5
print Solution().networkDelayTime(times, N, K)
