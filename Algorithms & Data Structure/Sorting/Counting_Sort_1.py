#ending index
'''
Sorting technuque based on keys b/w a specific range.
Counting the # of objects having distinct key values.
Do some arithmetic operations 
to calculate the position of each object
in the output sequence.
- Use a temporary array to store the result.
'''
#ascending
def countingSort(arr):
    N = len(arr)
    k = max(arr) # k is usaully given in the problem.
    count = [0] * (k+1) 
    temp = [0] * N

    for i in arr: #cumulative count
        count[i] += 1

    for i in range(1, k+1):
        count[i] += count[i-1]
    
    for i in range(N-1, -1, -1):
        count[arr[i]] -= 1 
        temp[count[arr[i]]] = arr[i]
