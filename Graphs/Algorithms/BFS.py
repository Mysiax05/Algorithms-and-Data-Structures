# adjacency list O(V+E) 
def bfs_list(G,s):
    from queue import Queue

    V = len(G)
    q = Queue()
    visited = [False] * V
    parent = [None] * V
    dist = [float('inf')] * V

    visited[s] = True
    dist[s] = 0
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                dist[v] = dist[u] + 1
                q.put(v)

    return visited, parent, dist

# adjacency matrix O(V^2)
def bfs_matrix(G,s):
    from queue import Queue

    V = len(G)
    q = Queue()
    visited = [False] * V
    parent = [None] * V
    dist = [float('inf')] * V

    visited[s] = True
    dist[s] = 0
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in range(V):
            if G[v][u] == 1 and not visited[v]:
                visited[v] = True
                parent[v] = u
                dist[v] = dist[u] + 1
                q.put(v)

    return visited, parent, dist