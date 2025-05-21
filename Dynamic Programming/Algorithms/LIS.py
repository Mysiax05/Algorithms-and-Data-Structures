# O(NlogN)
def lis(Tab):
    def binary_search_idx(tails,num):
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        return left
    # end def
    tails = []

    for num in Tab:
        idx = binary_search_idx(tails,num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)
