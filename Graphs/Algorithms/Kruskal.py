# edge list O(ElogV)
class Node:
    def __init__(self,value):
         self.val = value
         self.parent = self
         self.rank = 0
    
def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def make_set(v):
    return Node(v)

def kruskal(E):
    max_vertex = 0
    for u,v,w in E:
        max_vertex = max(max_vertex,u,v)

    E.sort(key=lambda v: v[2])
    MST = []
    V = [make_set(v) for v in range(max_vertex+1)]

    for u,v,w in E:
        if find(V[u]) != find(V[v]):
            MST.append((u,v,w))
            union(V[u],V[v])
    return MST

# NOTE
# This conversion is intended for use with Kruskal's algorithm
# !There are no duplicate edges!

# changing the representation of an adjacency list to an edge list O(V+E)
def from_adj_list_to_edge_list(G):
    V = len(G)
    E = []
    for u in range(V):
        for v,w in G[u]:
            if u < v:
                E.append((u,v,w))
    return E

# changing the representation of an adjacency matrix to an edge list(V^2)
def from_adj_matrix_to_edge_list(G):
    V = len(G)
    E = []
    for u in range(V):
        for v in range(u+1):
            if G[u][v] != float('inf'):
                E.append((u,v,G[u][v]))
    return E