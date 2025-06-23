from egz1btesty import runtests

def planets( D, C, T, E ):
    n = len(T)
    dp = [[float('inf') for _ in range(E+1)] for _ in range(n)]
    for x in range(E+1):
        dp[0][x] = x * C[0]
    dp[T[0][0]][0] = T[0][1]
    for i in range(1, n):
        if D[i] - D[i-1] <= E:
            dp[i][0] = min(dp[i][0], dp[i-1][D[i] - D[i-1]])
        dp[T[i][0]][0] = min(dp[T[i][0]][0], dp[i][0] + T[i][1])
        for e in range(1, E+1):
            if e + D[i] - D[i-1] <= E:
                without_tp = min(dp[i][e], dp[i-1][e + D[i] - D[i-1]], dp[i][e-1] + C[i])
            else:
                without_tp = min(dp[i][e], dp[i][e-1] + C[i])
            dp[i][e] = min(dp[i][e], without_tp)
    return min(dp[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )