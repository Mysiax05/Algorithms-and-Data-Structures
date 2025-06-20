from egz1atesty import runtests


def armstrong(B, G, s, t):
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
    # end def
    def bikes(B, V):
        speed = [1 for _ in range(V)]
        for u, p, q in B:
            speed[u] = min(speed[u], p/q)
        return speed
    #end def
    def dijkstra(G, s):
        V = len(G)
        q = PriorityQueue()
        visisted = [False for _ in range(V)]
        dist = [float('inf') for _ in range(V)]
        dist[s] = 0
        q.put((0, s))
        while not q.empty():
            d, u = q.get()
            if visisted[u]:
                continue
            visisted[u] = True
            for v, w in G[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    q.put((dist[v], v))
        return dist
    #end def
    G = change_to_adj_list(G)
    V = len(G)
    dist_with_bike = [0 for _ in range(V)]
    result = [0 for _ in range(V)]
    bike_speed = bikes(B, V)
    dist_from_start_to_bike = dijkstra(G, s)
    dist_from_bike_to_finish = dijkstra(G, t)
    for u in range(V):
        dist_with_bike[u] = dist_from_bike_to_finish[u] * bike_speed[u]
        if dist_from_start_to_bike[u] != float('inf') and dist_with_bike[u] != float('inf'):
            result[u] = int(dist_from_start_to_bike[u] + dist_with_bike[u])
        else:
            result[u] = float('inf')
    return min(result)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )