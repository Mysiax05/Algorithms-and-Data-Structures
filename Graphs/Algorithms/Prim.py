# adjacency list O(ElogV)
def prim_list(G,s):
    from queue import PriorityQueue
    V = len(G)
    q = PriorityQueue()
    visited = [False] * V
    parent = [None] * V
    weight = [float('inf')] * V

    weight[s] = 0
    q.put((0,s))
    while not q.empty():
        d,u = q.get()
        if visited[u]:
            continue
        visited[u] = True
        for v,w in G[u]:
            if not visited[v] and weight[v] > w:
                    weight[v] = w
                    parent[v] = u
                    q.put((w,v))
    return parent, sum(weight)

# adjacency matrix O(V^2)
def prim_matrix(G,s):
    from queue import PriorityQueue
    V = len(G)
    q = PriorityQueue()
    visited = [False] * V
    parent = [None] * V
    weight = [float('inf')] * V

    weight[s] = 0
    q.put((0,s))
    while not q.empty():
        d,u = q.get()
        if visited[u]:
             continue
        visited[u] = True
        for v,w in G[u]:
            if not visited[v] and weight[v] > w:
                weight[v] = w
                parent[v] = u
                q.put((w,v))
    return parent, sum(weight)