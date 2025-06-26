from egz3btesty import runtests

def uncool(P):
    def is_uncool(A, B):
        a1, b1 = A
        a2, b2 = B
        if b1 < a2 or b2 < a1:
            return False
        if (a1 <= a2 and b2 <= b1) or (a2 <= a1 and b1 <= b2):
            return False
        return True
    #end def
    n = len(P)
    for i in range(n):
        for j in range(i, n):
            if is_uncool(P[i], P[j]):
                return (i, j)


runtests(uncool, all_tests=True)