def mergeSort(arr, left, right):

    # base case
    if left >= right:
        return
    
    mid = (left + right) // 2

    mergeSort(arr, left, mid)
    mergeSort(arr, mid + 1, right)

    merge(arr, left, right, mid)


def merge(arr, left, right, mid):
    leftCopy = arr[left:mid+1]
    rightCopy = arr[mid + 1:right + 1]

    lCounter, rCounter = 0, 0
    sortedCounter = left

    while lCounter < len(leftCopy) and rCounter < len(rightCopy):
        if leftCopy[lCounter] <= rightCopy[rCounter]:
            arr[sortedCounter] = leftCopy[lCounter]
            lCounter += 1
        else:
            arr[sortedCounter] = rightCopy[rCounter]
            rCounter += 1
        sortedCounter += 1
    
    while lCounter < len(leftCopy):
        arr[sortedCounter] = leftCopy[lCounter]
        lCounter += 1
        sortedCounter += 1
    
    while rCounter < len(rightCopy):
        arr[sortedCounter] = rightCopy[rCounter]
        rCounter += 1
        sortedCounter += 1

