def Merge(T,p,q,r):
    n1 = q + 1 - p
    n2 = r - q
    L = [T[i+p] if i < n1 else float('inf') for i in range(n1+1)]
    R = [T[i+q+1] if i < n2 else float('inf') for i in range(n2+1)]

    i,j = 0,0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
    return
    
def Mergesort(T,p,r):
    if p < r:
        q = (p+r)//2
        Mergesort(T,p,q)
        Mergesort(T,q+1,r)
        Merge(T,p,q,r)
    return
