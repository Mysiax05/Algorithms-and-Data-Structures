#Lomuto version O(nlogn)
def lomuto_quicksort(T,p,r):
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
    if p < r:
        q = lomuto_partition(T, p, r)
        lomuto_quicksort(T, p, q-1)
        lomuto_quicksort(T, q+1, r)

#Hoare version O(nlogn)
from random import randint
def hoare_quicksort(T, p, r):
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
    if p < r:
        q = hoare_partition(T, p, r)
        hoare_quicksort(T, p, q)
        hoare_quicksort(T, q+1, r)