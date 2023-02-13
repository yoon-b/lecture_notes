'''
<pseudocode>
for i: N-1 -> 1
    for j: 0 -> i-1
        if a[j] > a[j+1]
            a[j] <-> a[j+1]
'''
#ascending
def BubbleSort(a, N): # a for List, N for len(a)
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
