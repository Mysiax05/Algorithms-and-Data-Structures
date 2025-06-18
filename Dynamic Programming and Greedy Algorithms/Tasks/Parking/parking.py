def parking(X,Y):
    n = len(X)
    m = len(Y)
    F = [[float('inf') for _ in range(m)] for _ in range(n)]
    F[0][0] = abs(X[0] - Y[0])

    for k in range(1, m):
        F[0][k] = min(F[0][k-1], abs(X[0] - Y[k]))

    for i in range(1, n):
        for j in range(i, m):
            F[i][j] = min(F[i][j-1], F[i-1][j-1] + abs(X[i] - Y[j]))

    return F[n-1][m-1]