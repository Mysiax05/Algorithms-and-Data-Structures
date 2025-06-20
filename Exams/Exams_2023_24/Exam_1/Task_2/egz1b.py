from egz1btesty import runtests


def kstrong(T, k):
    n = len(T)
    dp = [[-float('inf') for _ in range(k+1)] for _ in range(n)]
    dp[0][0] = T[0]
    for d in range(1, k+1):
        dp[0][d] = 0
    result = max(dp[0])
    for i in range(1, n):
        for d in range(k+1):
            take = dp[i-1][d] + T[i]
            dp[i][d] = max(take, T[i])
            if d > 0:
                dp[i][d] = max(dp[i][d], dp[i-1][d-1])
            result = max(result, dp[i][d])
    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )