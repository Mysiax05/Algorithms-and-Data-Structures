def subset_sum(A: list, S: int) -> bool:
    n = len(A)
    dp = [[False for _ in range(S+1)] for __ in range(n)]

    for x in range(n):
        dp[x][0] = True
    
    if A[0] <= S:
        dp[0][A[0]] = True

    for i in range(1, n):
        for s in range(1, S+1):
            dp[i][s] = dp[i-1][s]
            if s - A[i] >= 0:
                dp[i][s] = dp[i][s] or dp[i-1][s - A[i]]
    
    return dp[n-1][S]