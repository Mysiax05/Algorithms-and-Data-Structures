# Directed Acyclic Graph

# adjacency list O(V+E)
def top_sort_list(G,s):
    def dfs_visit(G,u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G,v)
        result.append(u)
    # end def
    V = len(G)
    visited = [False] * V
    result = []

    for u in range(V):
        if not visited[u]:
            dfs_visit(G,u)
    
    return result[::-1]