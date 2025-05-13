# adjacency list O(V+E)
def euler_list(G):
    from copy import deepcopy
    def dfs_check(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_check(G,v)
    # end def
    def dfs_visit(u):
        nonlocal graph, euler_cycle
        while graph[u]:
            v = graph[u].pop()
            graph[v].remove(u)
            dfs_visit(v)
        euler_cycle.append(u)
    # end def
    
    V = len(G)
    # checking if all vertices are of even degrees
    for u in range(V):
        if len(G[u]) % 2 == 1: return None
    # checking if graph is connected
    visited = [False] * V
    dfs_check(G,0)
    for v in range(V):
        if not visited[v]: return None

    #copying the graph so as not to overwrite the data
    graph = deepcopy(G)
    euler_cycle = []

    #setting start vertex
    s = next((i for i in range(V) if len(G[i]) > 0), None)
    if s is None:
        return []

    dfs_visit(s)
    
    return euler_cycle[::-1]

# adjacency matrix O(V^2)
def euler_matrix(G):
    from copy import deepcopy
    def dfs_check(G,u):
        visited[u] = True
        for v in range(len(G)):
            if G[u][v] == 1 and not visited[v]:
                dfs_check(G,v)
    # end def
    def dfs_visit(u):
        nonlocal graph, euler_cycle
        for v in range(len(G)):
            if graph[u][v] == 1:
                graph[u][v] = graph[v][u] = 0
                dfs_visit(v)
        euler_cycle.append(u)
    # end def
    
    V = len(G)
    # checking if all vertices are of even degrees
    for u in range(V):
        degree = sum(G[u])
        if degree % 2 != 0:
            return None
    # checking if graph is connected
    visited = [False] * V
    dfs_check(G,0)
    for v in range(V):
        if not visited[v]: return None

    #copying the graph so as not to overwrite the data
    graph = deepcopy(G)
    euler_cycle = []

    #setting start vertex
    s = next((i for i in range(V) if sum(G[i]) > 0), None)
    if s is None:
        return []

    dfs_visit(s)
    
    return euler_cycle[::-1]