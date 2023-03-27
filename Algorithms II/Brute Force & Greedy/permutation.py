def perm(i: int, k: int):  # p: 리스트, i: 값을 결정할 자리, k: 결정할 개수
    if i == k:
        print(*p)
    else:
        for j in range(i, k):  # 자신부터 오른쪽 원소들과 교환
            p[i], p[j] = p[j], p[i]
            perm(i+1, k)
            p[i], p[j] = p[j], p[i]
            
p = [1, 2, 3]
perm(0, 3)


# 사전순으로 배열된 순열 만들기
def perm2(i, k):
    if i == k:
        print(*p)
    else:
        for j in range(k):  # 자신부터 오른쪽 원소들과 교환
            if used[j] == 0:
                p[i] = [j]
                used[j] = 1
                perm2(i+1, k)
                used[j] = 0


used = [0] * len(p)