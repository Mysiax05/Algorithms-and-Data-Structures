def minimum_subset_sum_difference(A: list) -> int:
    n = len(A)
    S = sum(A)
    T = S // 2
    dp = [[False for _ in range(T+1)] for __ in range(n)]

    for i in range(n):
        dp[i][0] = True
    
    if A[0] <= T:
        dp[0][A[0]] = True

    for i in range(1, n):
        for t in range(1, T+1):
            dp[i][t] = dp[i-1][t]
            if t - A[i] >= 0:
                dp[i][t] = dp[i-1][t] or dp[i-1][t - A[i]]

    for t in range(T, -1, -1):
        if dp[n-1][t] == True:
            return (S - t) - t
    

print(minimum_subset_sum_difference([15, 21, 17, 8]))