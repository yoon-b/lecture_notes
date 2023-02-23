def minHeap(lst: list, i: int):
    left = 2 * i  # 왼쪽 노드
    right = 2 * i + 1  # 오른쪽 노드
    if left < len(lst) and lst[left] < lst[i]:
        minIdx = left
    else:
        minIdx = i

    if right < len(lst) and lst[right] < lst[minIdx]:
        minIdx = right

    if minIdx != i:
        lst[i], lst[minIdx] = lst[minIdx], lst[i]
        minHeap(lst, minIdx)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    heap = [0] + list(map(int, input().split()))
    for p in range(N//2, 0, -1):  # 마지막 부모 노드의 인덱스
        minHeap(heap, p)

    # 조상 노드들의 합
    ancestor = N//2
    sumA = 0
    while ancestor > 0:
        sumA += heap[ancestor]
        ancestor //= 2
    print(heap)
    print(f'#{tc}', sumA)
