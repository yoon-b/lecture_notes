'''
Find the minimum in the array and place it at the front.

<pseudocode>
for i from 0 to n-2
    a[i], ..., a[n-1] -> find min value in these
    swap a[i], a[k]
'''

def selectionSort(a, N): #a for array, N for len(a)
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N): #finding the min value
            if a[minIdx] > a[j]:
                minIdx = j
        
        a[i], a[minIdx] = a[minIdx], a[i]

def select(a, k): #a for array, k for kth minimum number
    for i in range(k):
        minIdx = i
        for j in range(i+1, len(a)):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
    
    return a[k-1] #k-1 cuz the index starts from 0