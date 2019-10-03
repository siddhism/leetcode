#
# @lc app=leetcode id=743 lang=python
#
# [743] Network Delay Time
#

# @lc code=start


class DSU(object):

    def __init__(self, N):
        from collections import defaultdict
        self.N = N
        self.parent = defaultdict(int)
        # initialize parent to self
        for i in range(N+1):
            self.parent[i] = i
        self.size = defaultdict(int)
        
    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)

        if self.size[root_a] < self.size[root_b]:
            self.parent[root_a] = root_b
            self.size[root_b] += 1 # size of root b increased
        else:
            self.parent[root_b] = root_a
            self.size[root_a] += 1

    def root(self, i):
        if self.parent[i] == i:
            return i
        # path compression
        self.parent[i] = self.root(self.parent[i])
        return self.parent[i]


class Solution(object):

    def dijkstra(self, graph, start, V):
        from heapq import heapify, heappush, heappop
        # initialize dist to inf for all nodes
        distances = {key: float('inf') for key in range(1, V+1)}
        # here i did this extra step to set initial value of v keys as well
        distances[start] = 0
        print distances

        # create a priority queue and push distances to it with connected nodes
        # format : distance, node
        pq = [(0, start)]
        while pq:
            current_distance, current_vertex = heappop(pq)

            # Nodes can get added to the priority queue multiple times. We only
            # process a vertex the first time we remove it from the priority queue.
            if current_distance > distances[current_vertex]:
                # we'll not consider this node if it already has a lower distance
                continue

            for v, w in graph[current_vertex]:
                # cur distance of v 
                new_distance = current_distance + w
                # Only consider this new path if it's better than any path we've
                # already found.
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    heappush(pq, (new_distance, v))

        return distances

    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # apply dijkstra and at the end sum all distances
        # create graph from given times array
        from collections import defaultdict
        # {'u': [(v, w), (v, w)]}
        self.graph = defaultdict(list)
        for u, v, w in times:
            self.graph[u].append((v, w))
        # print self.graph
        res = self.dijkstra(self.graph, K, N)
        print 'distances ', res
        if max(res.values()) == float('inf'):
            return -1
        return max(res.values())


        
# @lc code=end

print Solution().networkDelayTime(
    [[2,1,1],[2,3,1],[3,4,1]],
    4,
    2
)
print Solution().networkDelayTime(
    [[1,2,1],[2,1,3]],
    2,
    2
)
