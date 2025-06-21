from egz2atesty import runtests


def wired(T):
    n = len(T)
    memo = {}
    def f(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i > j:
            return 0
        if (j - i + 1) % 2 != 0:
            return float('inf')
        best = float('inf')
        for k in range(i+1, j+1, 2):
            cost = 1 + abs(T[i] - T[k])
            left = f(i+1, k-1)
            right = f(k+1, j)
            total = cost + left + right
            best = min(best, total)
        memo[(i, j)] = best
        return best
    return f(0, n-1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = True )