#O(nlogn)
def mergesort(T, p, r):
    def merge(T, p, q, r):
        A = T[p:r+1]
        k = p
        i = 0
        j = q - p + 1
        while i < q - p + 1 and j < r - p + 1:
            if A[i] < A[j]:
                T[k] = A[i]
                i += 1
            else:
                T[k] = A[j]
                j += 1
            k += 1
        while i < q - p + 1:
            T[k] = A[i]
            i += 1
            k += 1
        while j < r - p + 1:
            T[k] = A[j]
            j += 1
            k += 1
    #end def
    if p < r:
        q = (p + r) // 2
        mergesort(T, p, q)
        mergesort(T, q+1, r)
        merge(T, p, q, r)