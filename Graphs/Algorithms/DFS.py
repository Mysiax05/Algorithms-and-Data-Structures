# adjacency list O(V+E)
def dfs_list(G,s):
    def dfs_visit(G,u):
        nonlocal time
        visited[u] = True
        finish_time[u] = time
        time += 1

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(G,v)
    # end def
    V = len(G)
    time = 0
    visited = [False] * V
    parent = [None] * V
    finish_time = [float('inf')] * V

    dfs_visit(G,s)

    return visited, parent, finish_time

# adjacency matrix O(V^2)
def dfs_matrix(G,s):
    def dfs_visit(G,u):
        nonlocal time
        visited[u] = True
        finish_time[u] = time
        time += 1

        for v in range(len(G)):
            if G[u][v] == 1 and not visited[v]:
                parent[v] = u
                dfs_visit(G,v)
    # end def
    V = len(G)
    time = 0
    visited = [False] * V
    parent = [None] * V
    finish_time = [float('inf')] * V

    dfs_visit(G,s)

    return visited, parent, finish_time