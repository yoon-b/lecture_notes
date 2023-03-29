def quickSort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quickSort(arr, left, partition_pos - 1)
        quickSort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        # pivot값보다 큰 수 찾기
        while i < right and arr[i] < pivot:
            i += 1
        # pivot값보다 작은 수 찾기
        while j > left and arr[j] >= pivot:
            j -= 1
        # i, j 결정 후
        # i는 큰 값, j는 작은 값인데 인덱스는 i<j이므로 두 값을 바꿔줌
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # i, j 교차 (i<j가 성립하지 않으므로)
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i