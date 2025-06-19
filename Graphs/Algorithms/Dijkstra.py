# adjacency list O(ElogV) 
def dijkstra_list(G,s):
    from queue import PriorityQueue
    V = len(G)
    q = PriorityQueue()
    visited = [False] * V
    parent = [None] * V
    dist = [float('inf')] * V

    dist[s] = 0
    q.put((0,s))
    while not q.empty():
        d,u = q.get()
        if visited[u]:
            continue
        visited[u] = True
        for v,w in G[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
                q.put((dist[v],v))
    return dist, parent

# adjacency matrix O(V^2)
def dijkstra_matrix(G,s):
    from queue import PriorityQueue
    V = len(G)
    q = PriorityQueue()
    visited = [False] * V
    parent = [None] * V
    dist = [float('inf')] * V

    dist[s] = 0
    q.put((0,s))
    while not q.empty():
        d,u = q.get()
        if visited[u]:
            continue
        visited[u] = True
        for v in range(V):
            if G[u][v] != float('inf') and dist[v] > dist[u] + G[u][v]:
                parent[v] = u
                dist[v] = dist[u] + G[u][v]
                q.put((dist[v],v))
    return dist, parent