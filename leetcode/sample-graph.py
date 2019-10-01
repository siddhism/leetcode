def dfs(node):
    visited[node] = True
    print node
    for nxt in self.graph[node]:
        if not visited[nxt]:
            dfs(nxt)

dfs(root)


def bfs(node):
    queue = []
    queue.append(root)
    while queue:
        top = queue.pop(0)
        print top
        visited[top] = True
        for nxt in self.graph[top]:
            if not visited[nxt]:
                queue.append(top)
        

def dijkstra(graph, start):
    import heapq
    distances = {node: float('inf')) for node in graph}
    pq = [(0, start)]
    distances[start] = 0
    
    while pq:
        current_distance, node = heapq.heappop(pq)
        # check if this node is already visited and dist is min
        if current_distance > distances[node]:
            continue
        
        for nei, weight in graph[node].items():
            new_dist = current_distance + weight
            # iterate each neighbour if it's new_dist is less than existing
            # Only consider this new path if it's better than any path we've
            if new_dist < distances[nei]:
                heapq.heappush(pq, (new_dist, nei))
                distances[nei] = new_dist

    return distances