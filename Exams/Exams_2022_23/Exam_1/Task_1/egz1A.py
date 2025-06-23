from egz1Atesty import runtests

def gold(G,V,s,t,r):
    from queue import PriorityQueue
    n = len(G)
    q = PriorityQueue()
    cost = [[float('inf') for _ in range(n+1)] for _ in range(n)]
    visited = [[False for _ in range(n+1)] for _ in range(n)]
    cost[s][n] = 0
    q.put((0, n, s))
    while not q.empty():
        d, robbed, u = q.get()
        if visited[u][robbed]:
            continue
        visited[u][robbed] = True
        if robbed == n:
            cost[u][u] = d - V[u]
            q.put((cost[u][u], u, u))
        for v, w in G[u]:
            if robbed == n:
                if cost[v][n] > d + w:
                    cost[v][n] = d + w
                    q.put((cost[v][n], n, v))
            else:
                if cost[v][robbed] > d + 2*w + r:
                    cost[v][robbed] = d + 2*w + r
                    q.put((cost[v][robbed], robbed, v))
    return min(cost[t])
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )