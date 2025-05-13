# adjacency list O(V+E)
def top_sort_list(G):
    def dfs_visit(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G,v)
        result.append(u)
    # end def
    V = len(G)
    visited = [False] * V
    result = []

    for u in range(V):
        if not visited[u]:
            dfs_visit(G,u)
    
    return result[::-1]

# adjacency matrix O(V^2)
def top_sort_matrix(G):
    def dfs_vist(G,u):
        visited[u] = True
        for v in range(len(G)):
            if G[u][v] == 1 and not visited[v]:
                dfs_vist(G,v)
        result.append(u)
    # end def

    V = len(G)
    visited = [False] * V
    result = []

    for u in range(V):
        if not visited[u]:
            dfs_vist(G,u)
    
    return result[::-1]