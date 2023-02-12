#ending index
'''
Sorting technuque based on keys b/w a specific range.
Counting the # of onjects having distinct key values.
Do some arithmetic operations 
to calculate the position of each object
in the output sequence.
- Use a temporary array
'''
#ascending
def countingSort(arr):
    N = len(arr)
    count = [0] * (k+1) # k for the max value in the arr given.
    temp = [0] * N

    for i in arr: #cumulative count
        count[i] += 1

    for i in range(1, K+1):
        count[i] += count[i-1]
    
    for i in range(N-1, -1, -1):
        count[arr[i]] -= 1 
        temp[count[arr[i]]] = arr[i]
