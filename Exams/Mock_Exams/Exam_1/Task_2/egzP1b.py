from egzP1btesty import runtests 

def turysta( G, D, L ):
    from queue import PriorityQueue
    def change_to_adj_list(G):
        max_vertex = 0
        for u, v, w in G:
            max_vertex = max(max_vertex, u, v)
        V = max_vertex + 1
        graph = [[] for _ in range(V)]
        for u, v, w in G:
            graph[u].append((v, w))
            graph[v].append((u, w))
        return graph
    #end def
    G = change_to_adj_list(G)
    V = len(G)
    q = PriorityQueue()
    visited = [[False for _ in range(4)] for __ in range(V)]
    dist = [[float('inf') for _ in range(4)] for __ in range(V)]
    dist[D][0] = 0
    q.put((0, 0, D))
    while not q.empty():
        d, t, u = q.get()
        if visited[u][t]:
            continue
        visited[u][t] = True
        for v, w in G[u]:
            if t == 3 and v == L:
                if dist[v][t] > d + w:
                    dist[v][t] = d + w
            if t < 3 and dist[v][t] > d + w:
                dist[v][t] = d + w
                q.put((dist[v][t], t+1, v))
    return dist[L][3]

runtests ( turysta )