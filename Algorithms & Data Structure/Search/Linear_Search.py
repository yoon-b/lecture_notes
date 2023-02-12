#Linear search a.k.a. sequential search

# with unsorted arr
# a for arr, N for len(a), searching key
def linearSearch(a, N, key):
    i = 0
    
    while i < N and a[i] != key:
        i += 1
    
    if i < N:
        return i
    else:
        return 'Not Found'
    
# with sorted arr in ascending order
def linearSearch2(a, N, key):
    i = 0

    while i < N and a[i] < key:
        i += 1
    
    if i < N and a[i] == key:
        return i
    else:
        return 'Not Found'