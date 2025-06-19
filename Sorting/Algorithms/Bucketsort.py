#Version for numbers in range(0, 1) O(n + k)
def bucketsort_0_1(T):
    def insertion_sort(T):
        n = len(T)
        for i in range(1, n):
            j = i - 1
            while j >= 0 and T[j] > T[i]:
                T[j+1] = T[j]
                j -= 1
            T[j+1] = T[i]
    #end def
    n = len(T)
    buckets = [[] for _ in range(n)]
    for i in range(n):
        idx = int(T[i] * n)
        buckets[idx].append(T[i])
    for bucket in buckets:
        insertion_sort(bucket)
    idx = 0
    for bucket in buckets:
        for num in bucket:
            T[idx] = num
            idx += 1
 
#Version for any range of numbers O(n + k)
def bucketsort(T):
    def insertion_sort(T):
        n = len(T)
        for i in range(n):
            j = i - 1
            while j >= 0 and T[j] > T[i]:
                T[j+1] = T[j]
                j -= 1
            T[j+1] = T[i]
    #end def
    n = len(T)
    buckets = [[] for _ in range(n)]
    min_num = min(T)
    max_num = max(T)
    range_val = max_num - min_num + 1
    for i in range(n):
        norm = (T[i] - min_num) / range_val
        idx = int(norm * n)
        if idx == n:
            idx = n-1
        buckets[idx].append(T[i])
    for bucket in buckets:
        insertion_sort(bucket)
    idx = 0
    for bucket in buckets:
        for num in bucket:
            T[idx] = num
            idx += 1