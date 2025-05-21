# O(N)
class Independent_set:
    def __init__(self,value):
        self.subtree = []
        self.val = value
        self.t = -1
        self.nt = -1

def max_independent_set(v):
    def taken(v):
        if v.t >= 0: return v.t
        x = not_taken(v)
        y = v.val
        for u in v.subtree:
            y += not_taken(u)
        v.t = max(x,y)
        return v.t
    # end def
    def not_taken(v):
        if v.nt >= 0: return v.nt
        v.nt = 0
        for u in v.subtree:
            v.nt += taken(u)
        return v.nt
    # end def
    return max(taken(v),not_taken(v))