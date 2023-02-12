
# p for searching pattern, t for the whole text
def bruteForce(t, p):
    N = len(t)
    M = len(p)
    idxT, idxP = 0, 0

    while idxP < M and idxT < N:
        if t[idxT] != p[idxP]:
            idxT -= idxP
            idxP = -1
        idxP += 1
        idxT += 1

    if idxP == M:
        return idxT - M
    else:
        return "Not Found"        
        


