from egz2btesty import runtests


from collections import deque
def tory_amos(E, A, B):
    def change_to_adj_list(E):
        max_vertex = 0
        for u, v, w, typ in E:
            max_vertex = max(max_vertex, u, v)
        V = max_vertex + 1
        G = [[] for _ in range(V)]
        for u, v, w, typ in E:
            G[u].append((v, w, typ))
            G[v].append((u, w, typ))
        return G

    def cost(typ, new_typ):
        if typ != new_typ:
            if typ != 0:
                return 20
            return 0
        return 5 if typ == 'I' else 10

    G = change_to_adj_list(E)
    V = len(G)
    dist = [{} for _ in range(V)]
    q = deque()
    dist[A][0] = 0
    q.appendleft((A, 0))

    while q:
        u, typ = q.popleft()
        d_u = dist[u][typ]
        for v, w, new_typ in G[u]:
            c = cost(typ, new_typ)
            new_dist = d_u + w + c
            d_v = dist[v].get(new_typ, float('inf'))
            if new_dist < d_v:
                dist[v][new_typ] = new_dist
                if c == 0:
                    q.appendleft((v, new_typ))
                else:
                    q.append((v, new_typ))

    return min(dist[B].values(), default=-1)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )