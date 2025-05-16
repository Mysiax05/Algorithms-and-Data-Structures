# adjacency list O(V+E)
def bridges_list(G):
    def dfs(G,u):
        nonlocal d
        visited[u] = True
        dist[u] = low[u] = d
        d += 1
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs(G,v)
                low[u] = min(low[u],low[v])
                if low[v] == dist[v]:
                    bridges.append((u,v))
            elif v != parent[u]:
                low[u] = min(low[u], dist[v])
    # end def
    V = len(G)
    visited = [False] * V
    parent = [None] * V
    dist = [float('inf')] * V
    low = [float('inf')] * V
    d = 0
    
    bridges = []
    for u in range(V):
        if not visited[u]:
            dfs(G,u)
    
    return bridges

# adjacency matrix O(V^2)
def bridges_matrix(G):
    def dfs(G,u):
        nonlocal d
        visited[u] = True
        dist[u] = low[u] = d
        d += 1
        for v in range(len(G)):
            if G[u][v] == 1 and not visited[v]:
                parent[v] = u
                dfs(G,v)
                low[u] = min(low[u],low[v])
                if low[v] == dist[v]:
                    bridges.append((u,v))
            elif G[u][v] == 1 and v != parent[u]:
                low[u] = min(low[u], dist[v])
    # end def
    V = len(G)
    visited = [False] * V
    parent = [None] * V
    dist = [float('inf')] * V
    low = [float('inf')] * V
    d = 0
    
    bridges = []
    for u in range(V):
        if not visited[u]:
            dfs(G,u)
    
    return bridges