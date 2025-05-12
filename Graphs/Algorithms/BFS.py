# adjacency list O(V+E)
from queue import Queue
def bfs_list(G,s):
    queue = Queue()
    V = len(G)
    visited = [False] * V
    parent = [None] * V
    distance = [float('inf')] * V

    visited[s] = True
    distance[s] = 0
    queue.put(s)

    while not queue.empty():
        v = queue.get()
        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                distance[u] = distance[v] + 1
                visited[u] = True
                queue.put(u)
    return visited,parent,distance

# adjacency matrix O(V^2)
def bfs_matrix(G,s):
    queue = Queue()
    V = len(G)
    visited = [False] * V
    parent = [None] * V
    distance = [float('inf')] * V

    visited[s] = True
    distance[s] = 0
    queue.put(s)

    while not queue.empty():
        v = queue.get()
        for u in range(V):
            if G[v][u] == 1 and not visited[u]:
                parent[u] = v
                distance[u] = distance[v] + 1
                visited[u] = True
                queue.put(u)
    return visited,parent,distance

list = [[1,2],[0,4,5],[0,3,4],[2,6],[1,2,6],[1,6],[3,4,5]]

matrix = [[0,1,1,0,0,0,0],
          [1,0,0,0,1,1,0],
          [1,0,0,1,1,0,0],
          [0,0,1,0,0,0,1],
          [0,1,1,0,0,0,1],
          [0,1,0,0,0,0,1],
          [0,0,0,1,1,1,0]]

print(bfs_list(list,0))
print(bfs_matrix(matrix,0))