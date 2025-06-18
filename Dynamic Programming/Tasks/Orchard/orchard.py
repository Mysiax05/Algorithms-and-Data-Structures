def orchard(T, m):
    n = len(T)
    dp = [[float('inf') for _ in range(m)] for _ in range(n+1)]

    dp[0][0] = 0

    for i in range(1, n+1):
        for r in range(m):
            dp[i][r] = min(dp[i][r], dp[i-1][r] + 1)

            new_r = (r + T[i-1]) % m
            dp[i][new_r] = min(dp[i][new_r], dp[i-1][r])

    return dp[n][0]