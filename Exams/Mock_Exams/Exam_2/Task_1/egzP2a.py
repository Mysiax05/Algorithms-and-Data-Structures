from egzP2atesty import runtests 

def zdjecie(T, m, k):
    from random import randint
    def quickselect(T, p, r, k):
        def partition(T, p, r):
            pivot = T[randint(p, r)][1]
            i = p - 1
            j = r + 1
            while True:
                i += 1
                while T[i][1] > pivot:
                    i += 1
                j -= 1
                while T[j][1] < pivot:
                    j -= 1
                if i >= j:
                    return j
                T[i], T[j] = T[j], T[i]
        #end def
        if p < r:
            q = partition(T, p, r)
            if k <= q:
                quickselect(T, p, q, k)
            else:
                quickselect(T, q+1, r, k)
    #end def
    n = len(T)
    row = k + m - 2
    start = [0]
    end = [row]
    for _ in range(m-1):
        start.append(end[-1] + 1)
        end.append(start[-1] + row-1)
        row -= 1
    for i in range(m-1):
        quickselect(T, 0, n-1, end[i])
    A = T[:n]
    items = 0
    for i in range(m+k-1):
        for j in range(m):
            idx = start[j] + i
            if idx <= end[j]:
                T[items] = A[idx]
                items += 1
    return None


runtests ( zdjecie, all_tests=False )