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
        
# counting the pattern's appearance
def bruteForceCount(t, p):
    N = len(t)
    M = len(p)
    idxT, idxP, cnt = 0, 0, 0

    while idxT < N:
        if t[idxT] != p[idxP]:
            idxT -= idxP
            idxP = -1
        idxP += 1
        idxT += 1

        if idxP == M:
            idxP = 0
            cnt += 1
    
    if cnt:
        return cnt
    else:
        return "Not Found"


# example
# t = 'abdfaa'
# p = 'a'
# print(bruteForce(t, p))
# print(bruteForceCount(t, p))