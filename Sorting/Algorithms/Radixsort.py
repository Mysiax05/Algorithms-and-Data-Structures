#O(d*(n+b))
def radixsort(T):
    def countingsort(T, exp): #O(n)
        n = len(T)
        count_T = [0 for _ in range(10)]
        res_T = [0 for _ in range(n)]
        for i in range(n):
            idx = T[i] // exp
            count_T[idx % 10] += 1
        for i in range(1, 10):
            count_T[i] += count_T[i-1]
        i = n-1
        while i >= 0:
            idx = T[i] // exp
            res_T[count_T[idx % 10] - 1] = T[i]
            count_T[idx % 10] -= 1
            i -= 1
        for i in range(n):
            T[i] = res_T[i]
    #end def
    max_num = max(T)
    exp = 1
    while max_num / exp >= 1:
        countingsort(T, exp)
        exp *= 10