# O(n^3)
from math import sqrt
def bttsp(Towns):
    def dist(i,j):
        xi,yi = i[0],i[1]
        xj,yj = j[0],j[1]
        return sqrt((xi-xj)**2 + (yi-yj)**2)
    # end def
    Towns = sorted(Towns, key=lambda x: x[0])
    n = len(Towns)
    D = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                D[i][j] = dist(Towns[i],Towns[j])

    F = [[float('inf')] * n for _ in range(n)]
    F[0][1] = D[0][1]

    def tspf(i,j):
        if F[i][j] != float('inf'): 
            return F[i][j]
        if i == j - 1:
            best = float('inf')
            for k in range(j-1):
                best = min(best, tspf(k, j-1) + D[k][j])
            F[j-1][j] = best
        else:
            F[i][j] = tspf(i, j-1) + D[j-1][j]
        return F[i][j]
    
    return tspf(n-2, n-1)