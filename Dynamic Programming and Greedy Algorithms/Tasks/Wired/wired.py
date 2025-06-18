def wired(T):
    n = len(T)
    memo = {}

    def f(i, j):
        if i >= j:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        best = float('inf')

        for k in range(i + 1, j + 1, 2):
            left = f(i + 1, k - 1)
            right = f(k + 1, j)
            cost = 1 + abs(T[i] - T[k])
            best = min(best, left + right + cost)

        memo[(i, j)] = best
        return best

    return f(0, n - 1)