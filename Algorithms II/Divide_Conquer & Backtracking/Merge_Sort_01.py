def mergeSort1(m: list):
    # 분할한 리스트를 모두 저장해야하므로 비효율적
    if len(m) == 1:
        return m
    middle = len(m)//2
    left = m[:middle]
    right = m[middle:]

    left = mergeSort1(left)
    right = mergeSort1(right)
    return merge(left, right)


def merge(left, right):
    pass


def mergeSort2(start, end):
    # 리스트의 인덱스로 접근. 리스트의 중복 생성을 방지
    # temp list 필요
    if start == end:
        return
    middle = (start + end)//2
    mergeSort2(start, middle)
    mergeSort2(middle+1, end)
    t = 0  # temp의 인덱스
    # merge
    left, right = start, middle+1  # 왼쪽과 오른쪽에서 가장 작은 숫자의 위치. 좌우는 이미 정렬된 상태
    while left <= middle or right <= end:
        if left <= middle and right <= end:
            if arr[left]<=arr[right]:
                temp[t] = arr[left]
                left += 1
            else:
                temp[t] = arr[right]
                right += 1
            t += 1
        elif left <= middle:
            while left <= middle:
                temp[t] = arr[left]
                left += 1
                t += 1
        elif right <= end:
            while right <= end:
                temp[t] = arr[right]
                right += 1
                t += 1
    i = 0
    while i < t:
        arr[start+i] = temp[i]
        i += 1
    return    


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    temp = [0] * N
    # mergeSort1(arr)
    mergeSort2(0, N-1)