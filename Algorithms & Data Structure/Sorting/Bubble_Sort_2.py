'''
Repeatedly swapping the consecutive items 
if they are in the wrong order.

The highest number will bubble its way to the right
with each iteration.
'''
'''
<pseudocode>
for i from 0 to N-1 # repeat for the length of an array
    for j from 0 to N-i-1 #Last i elements are already in place
        if a[j]> a[j+1]
            swap (a[j], a[j+1])
'''

def bubbleSort(arr):
    N = len(arr)

    for i in range(N):
        for j in range(N-i-1): #traverse the arr
            if arr[j] > arr[j+1]: #if the element found is greater than the next one,
                arr[j], arr[j+1] = arr[j+1], arr[j] #swap