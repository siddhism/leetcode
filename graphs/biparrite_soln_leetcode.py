# Python3 program to find out whether a 
# given graph is Bipartite or not 

class Graph(): 

    def __init__(self, V): 
        self.V = V 
        self.graph = [[0 for column in range(V)] 
                        for row in range(V)] 

        self.colorArr = [-1 for i in range(self.V)] 
        

    def add_edge(self, u, v):
        self.graph[u][v] = 1

    # This function returns true if graph G[V][V] 
    # is Bipartite, else false 
    def isBipartiteUtil(self, src): 

        # Create a color array to store colors 
        # assigned to all veritces. Vertex 
        # number is used as index in this array. 
        # The value '-1' of self.colorArr[i] is used 
        # to indicate that no color is assigned to 
        # vertex 'i'. The value 1 is used to indicate 
        # first color is assigned and value 0 
        # indicates second color is assigned. 

        # Assign first color to source 

        # Create a queue (FIFO) of vertex numbers and 
        # enqueue source vertex for BFS traversal 
        queue = [] 
        queue.append(src) 

        # Run while there are vertices in queue 
        # (Similar to BFS) 
        while queue: 

            u = queue.pop() 

            # Return false if there is a self-loop 
            if self.graph[u][u] == 1: 
                return False; 

            for v in range(self.V): 

                # An edge from u to v exists and 
                # destination v is not colored 
                if (self.graph[u][v] == 1 and
                    self.colorArr[v] == -1): 

                    # Assign alternate color to 
                    # this adjacent v of u 
                    self.colorArr[v] = 1 - self.colorArr[u] 
                    queue.append(v) 

                # An edge from u to v exists and destination 
                # v is colored with same color as u 
                elif (self.graph[u][v] == 1 and
                    self.colorArr[v] == self.colorArr[u]): 
                    return False

        # If we reach here, then all adjacent 
        # vertices can be colored with alternate 
        # color 
        return True
        
    def isBipartite(self): 
        self.colorArr = [-1 for i in range(self.V)] 
        for i in range(self.V): 
            if self.colorArr[i] == -1: 
                if not self.isBipartiteUtil(i): 
                    return False
        return True
                    
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        g = Graph(len(graph))
        for node_index, dests in enumerate(graph):
            for dest in dests:
                g.add_edge(node_index, dest)

        return g.isBipartite(0)
