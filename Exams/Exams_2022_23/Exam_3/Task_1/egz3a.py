from egz3atesty import runtests

def goodknight( G, s, t ):
  from collections import deque
  V = len(G)
  q = deque()
  visited = [[False for _ in range(17)] for _ in range(V)]
  dist = [[float('inf') for _ in range(17)] for _ in range(V)]
  dist[s][0] = 0
  q.append((0, 0, s))
  while q:
    d, fatigue, u = q.popleft()
    if visited[u][fatigue]:
      continue
    visited[u][fatigue] = True
    for v in range(V):
      if G[u][v] != -1:
        if fatigue + G[u][v] > 16:
          new_dist = d + G[u][v] + 8
          new_fatigue = G[u][v]
        else:
          new_dist = d + G[u][v]
          new_fatigue = fatigue + G[u][v]
        if dist[v][new_fatigue] > new_dist:
          dist[v][new_fatigue] = new_dist
          q.append((new_dist, new_fatigue, v))
  return min(dist[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )