def permute(i, k):
    if i == k:
        # 순열 완성 후 여기서 관련 작업 가능
        print(p)
    else:
        for j in range(i, k):  # i+1을 하지 않는 이유?
            p[i], p[j] = p[j], p[i]
            # p[i]가 결정됐으므로, p[i]와 관련된 작업 가능
            permute(i+1, k)
            p[i], p[j] = p[j], p[i]


p = [1, 2, 3]
N = len(p)
permute(0, N)

"""
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 2, 1]
[3, 1, 2]
사전순으로 출력되지 X
사전순 출력 -> 앞에서 사용하고 남은 애들로 순열을 만들어야 함
"""