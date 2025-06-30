from collections import deque

class WeightedBFS:
    def __init__(self):
        self.q = deque()

    def push(self, node, dist):
        self.q.append((node, dist))

    def run(self, G, start, max_d):
        V = len(G)
        dist = [float('inf')] * V
        dist[start] = 0
        self.q.append((start, 0))

        while self.q:
            u, d_u = self.q.popleft()
            if d_u > dist[u]:
                continue
            for v, cost in G[u]:
                d_v = d_u + cost
                if d_v < dist[v]:
                    dist[v] = d_v
                    if cost == 0:
                        self.q.appendleft((u, d_v))
                    else:
                        self.q.append((u, d_v))
        return dist