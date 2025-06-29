# adjacency list O(ElogV)
def prim_list(G,s):
    from queue import PriorityQueue
    V = len(G)
    q = PriorityQueue()
    visited = [False] * V
    parent = [None] * V
    weight = [float('inf')] * V
    total_sum = 0

    weight[s] = 0
    q.put((0,s))
    while not q.empty():
        d,u = q.get()
        if visited[u]:
            continue
        total_sum += d
        visited[u] = True
        for v,w in G[u]:
            if not visited[v] and weight[v] > w:
                    weight[v] = w
                    parent[v] = u
                    q.put((w,v))
    return parent, total_sum

# adjacency matrix O(V^2)
def prim_matrix(G,s):
    V = len(G)
    visited = [False] * V
    parent = [None] * V
    weight = [float('inf')] * V
    total_weight = 0

    weight[s] = 0
    for _ in range(V):
        u = -1
        min_weight = float('inf')
        for v in range(V):
            if not visited[v] and weight[v] < min_weight:
                min_weight = weight[v]
                u = v
        
        if u == -1:
            break

        total_weight += weight[u]
        visited[u] = True
        for v in range(V):
            if G[u][v] != float('inf') and weight[v] > G[u][v]:
                weight[v] = G[u][v]
                parent[v] = u
    return parent, total_weight