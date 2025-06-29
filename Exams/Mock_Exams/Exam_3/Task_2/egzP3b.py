from egzP3btesty import runtests 

def lufthansa ( G ):
    from queue import PriorityQueue
    def prim(G):
        V = len(G)
        q = PriorityQueue()
        visited = [False for _ in range(V)]
        weight = [-float('inf') for _ in range(V)]
        parent = [None for _ in range(V)]
        total_weight= 0
        weight[0] = 0
        q.put((0, 0))
        while not q.empty():
            d, u = q.get()
            if visited[u]:
                continue
            total_weight += d
            visited[u] = True
            for v,w in G[u]:
                if not visited[v] and weight[v] < w:
                    parent[v] = u
                    weight[v] = w
                    q.put((-weight[v], v))
        return parent, total_weight
    #end def
    V = len(G)
    total = 0
    path, res = prim(G)
    max_unused = 0
    for u in range(V):
        for v, w in G[u]:
            total += w
            if path[u] == v or path[v] == u:
                continue
            max_unused = max(max_unused, w)
    return total//2 - (res + max_unused)


runtests ( lufthansa, all_tests=True )