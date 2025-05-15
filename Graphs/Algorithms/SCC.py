# adjacency list O(V+E)
def scc_list(G):
    def dfs_forward(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_forward(G,v)
        order.append(u)
        return
    # end def
    def transpose_graph(G):
        V = len(G)
        GT = [[] for _ in range(V)]
        for u in range(V):
            for v in G[u]:
                GT[v].append(u)
        return GT
    # end def
    def dfs_backward(GT,u,component):
        visited[u] = True
        component.append(u)
        for v in GT[u]:
            if not visited[v]:
                dfs_backward(G,v,component)
        return
    # end def

    V = len(G)
    visited = [False] * V
    order = []

    for u in range(V):
        if not visited[u]:
            dfs_forward(G,u)
    
    GT = transpose_graph(G)

    visited = [False] * V
    scc = []
    for u in reversed(order):
        if not visited[u]:
            component = []
            dfs_backward(GT,u,component)
            scc.append(component)
    
    return scc

# adjacency matrix O(V^2)
def scc_matrix(G):
    def dfs_forward(G,u):
        visited[u] = True
        for v in range(len(G)):
            if G[u][v] == 1 and not visited[v]:
                dfs_forward(G,v)
        order.append(u)
        return
    # end def
    def transpose_graph(G):
        V = len(G)
        GT = [[0 for _ in range(V)] for _ in range(V)]
        for u in range(V):
            for v in range(V):
                if G[u][v] == 1:
                    GT[v][u] = 1
        return GT
    # end def
    def dfs_backward(GT,u,component):
        visited[u] = True
        component.append(u)
        for v in range(len(GT)):
            if GT[u][v] == 1 and not visited[v]:
                dfs_backward(GT,v,component)
        return
    # end def

    V = len(G)
    visited = [False] * V
    order = []

    for u in range(V):
        if not visited[u]:
            dfs_forward(G,u)
    
    GT = transpose_graph(G)

    visited = [False] * V
    scc = []
    for u in reversed(order):
        if not visited[u]:
            component = []
            dfs_backward(GT,u,component)
            scc.append(component)
    
    return scc