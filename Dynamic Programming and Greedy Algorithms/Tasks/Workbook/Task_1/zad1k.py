from zad1ktesty import runtests

def roznica( S ):
    if '0' not in S:
        return -1
    n = len(S)
    dp = [0 for _ in range(n)]
    dp[0] = 1 - int(S[0])
    for i in range(1, n):
        if int(S[i]) == 0:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = max(dp[i-1] - 1, 0)
    return max(dp)

runtests ( roznica )