# edge list O(VE)
def bellman_ford(E,s):
    max_vertex = 0
    for u,v,w in E:
        max_vertex = max(max_vertex,u,v)
    V = max_vertex + 1
    dist = [float('inf')] * V

    dist[s] = 0
    for _ in range(V-1):
        for u,v,w in E:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
            
    for u,v,w in E:
        if dist[v] > dist[u] + w:
            return None
    
    return dist

# ATTENTION!
# This conversion is intended for use with the Bellman-Ford algorithm only
# !If the graph is undirected, duplicate edges are created, such as: (4,2,0) and (2,4,0)!

# changing the representation of an adjacency list to an edge list O(V+E)
def from_adj_list_to_edge_list(G):
    V = len(G)
    E = []
    for u in range(V):
        for v,w in G[u]:
            E.append((u,v,w))
    return E

# changing the representation of an adjacency matrix to an edge list(V^2)
def from_adj_matrix_to_edge_list(G):
    V = len(G)
    E = []
    for u in range(V):
        for v in range(V):
            if G[u][v] != float('inf'):
                E.append((u,v,G[u][v]))
    return E