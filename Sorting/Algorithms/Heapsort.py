#O(nlogn)
def heapsort(T):
    def parent(i):
        return (i-1)//2
    #end def
    def left(i):
        return 2*i + 1
    #end def
    def right(i):
        return 2*(i+1)
    #end def
    def build_heap(T):
        n = len(T)
        for i in range(parent(n-1), -1, -1):
            heapify(T, n, i)
    #end def
    def heapify(T, n, i):
        l = left(i)
        p = right(i)
        max_idx = i
        if l < n and T[l] > T[max_idx]:
            max_idx = l
        if p < n and T[p] > T[max_idx]:
            max_idx = p
        if max_idx != i:
            T[i], T[max_idx] = T[max_idx], T[i]
            heapify(T, n, max_idx)
    #end def
    n = len(T)
    build_heap(T)
    for i in range(n-1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)