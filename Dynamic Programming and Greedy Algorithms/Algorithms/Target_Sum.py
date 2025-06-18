def target_sum(A: list, T: int) -> int:
    n = len(A)
    S = sum(A)
    if (S + T) % 2 == 1 or S < abs(T):
        return 0
    
    P = (S + T) // 2

    dp = [[0 for _ in range(P+1)] for __ in range(n)]

    for i in range(n):
        dp[i][0] = 1
    
    if A[0] <= P:
        dp[0][A[0]] = 1
    
    for i in range(1, n):
        for p in range(1, P+1):
            dp[i][p] = dp[i-1][p]
            if p - A[i] >= 0:
                dp[i][p] = dp[i-1][p] + dp[i-1][p-A[i]]

    return dp[n-1][P]