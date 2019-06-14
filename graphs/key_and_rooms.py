from collections import defaultdict

class Graph:

    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V
        self.visited = [False for _ in range(self.V + 1)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, u):
        self.visited[u] = True
        # print u,
        for neighbour in self.graph[u]:
            if not self.visited[neighbour]:
                self.DFSUtil(neighbour)

    def DFS(self, u):
        self.DFSUtil(u)

    def print_graph(self):
        for k, v in self.graph.items():
            print k, ' -> ', v


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # build graph
        graph = Graph(len(rooms))
        for room_index, keys  in enumerate(rooms):
            for key in keys:
                graph.add_edge(room_index, key)
        # graph.print_graph()
        graph.DFS(0)
        all_visited = True
        for i in range(len(rooms)):
            if not graph.visited[i]:
                all_visited = False
                break
        return all_visited

