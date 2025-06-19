#O(n + k)
def countingsort(T):
    n = len(T)
    k = max(T)
    count_T = [0 for _ in range(k + 1)]
    res_T = [0 for _ in range(n)]
    for i in range(n):
        count_T[T[i]] += 1
    for i in range(1, k+1):
        count_T[i] += count_T[i-1]
    for i in range(n-1, -1, -1):
        res_T[count_T[T[i]] - 1] = T[i]
        count_T[T[i]] -= 1
    return res_T