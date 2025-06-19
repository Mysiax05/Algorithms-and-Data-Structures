#Lomuto version O(n)
def lomuto_quickselect(T, p, r, k):
    def lomuto_partition(T, p, r):
        pivot = T[r]
        i = p-1
        for j in range(p, r):
            if T[j] <= pivot:
                i += 1
                T[i], T[j] = T[j], T[i]
        T[i+1], T[r] = T[r], T[i+1]
        return i+1
    #end def
    if p == r:
        return T[p]
    idx = lomuto_partition(T, p, r)
    if k == idx - p + 1:
        return T[idx]
    elif k < idx - p + 1:
        return lomuto_quickselect(T, p, idx - 1, k)
    else:
        return lomuto_quickselect(T, idx + 1, r, k - (idx - p + 1))
 
#Hoare version O(n)
from random import randint
def hoare_quickselect(T, p, r, k):
    def hoare_partition(T, p, r):
        pivot = T[randint(p, r)]
        i = p - 1
        j = r + 1
        while True:
            i += 1
            while T[i] < pivot:
                i += 1
            j -= 1
            while T[j] > pivot:
                j -= 1
            if i >= j:
                return j
            T[i], T[j] = T[j], T[i]
    #end def
    if p == r:
        return T[p]
    idx = hoare_partition(T, p, r)
    if k <= idx - p + 1:
        return hoare_quickselect(T, p, idx, k)
    else:
        return hoare_quickselect(T, idx + 1, r, k - (idx - p + 1))