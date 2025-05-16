# adjacency matrix O(V^3)
def floyd_warshall(G):
    V = len(G)
    dist = [[G[u][v] if u != v else 0 for v in range(V)] for u in range (V)]
    for k in range(V):
        for u in range(V):
            for v in range(V):
                if dist[u][k] != float('inf') and dist[k][v] != float('inf'):
                    dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])
    return dist

# convert adjacency list to adjacency matrix O(V^2)
def from_list_to_matrix(G):
    V = len(G)
    matrix = [([float('inf')] * V) for _ in range(V)]
    for u in range(V):
        for v,w in G[u]:
            matrix[u][v] = w
    return matrix