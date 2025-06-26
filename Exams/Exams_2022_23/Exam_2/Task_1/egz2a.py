from egz2atesty import runtests

def dominance(P):
    n=len(P)
    dp = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if P[j][0] > P[i][0] and P[j][1] > P[i][1]:
                dp[j] += 1
    return max(dp)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )