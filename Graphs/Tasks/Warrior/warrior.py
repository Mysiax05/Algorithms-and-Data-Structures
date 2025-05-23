def warrior(G,s,t):
    def change_edge_list_to_adj_list(G,V):
        graph = [[] for _ in range(V)]
        for u,v,w in G:
            graph[u].append((v,w))
            graph[v].append((u,w))
        return graph
    #end def
    from queue import PriorityQueue
    max_vertex = 0
    for u,v,w in G:
        max_vertex = max(max_vertex, u, v)
    V = max_vertex + 1

    q = PriorityQueue()
    visited = [[False] * 17 for _ in range(V)]
    dist = [[float('inf')] * 17 for _ in range(V)] 
    graph = change_edge_list_to_adj_list(G,V)

    dist[s][0] = 0
    q.put((0, 0, s))
    while not q.empty():
        d, fatigue, u = q.get()
        if visited[u][fatigue]:
            continue
        visited[u][fatigue] = True
        for v, w in graph[u]:
            if not visited[v][fatigue]:
                if fatigue + w > 16:
                    new_fatigue = w
                    new_d = d + w + 8
                else:
                    new_fatigue = fatigue + w
                    new_d = d + w
                if dist[v][new_fatigue] > new_d:
                    dist[v][new_fatigue] = new_d
                    q.put((new_d, new_fatigue, v))

    return min(dist[t])