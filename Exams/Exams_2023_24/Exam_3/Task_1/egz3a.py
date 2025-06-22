from egz3atesty import runtests

from queue import Queue
def mykoryza( G,T,d ):
  result = 1
  V = len(G)
  q = Queue()
  parent = [None for _ in range(V)]
  visited = [False for _ in range(V)]
  for u in T:
    q.put(u)
    parent[u] = u
    visited[u] = True
  while not q.empty():
    u = q.get()
    for v in G[u]:
        if not visited[v]:
          visited[v] = True
          parent[v] = parent[u]
          if parent[v] == T[d]:
            result += 1
          q.put(v)
  return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )