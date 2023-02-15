
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


# how store path info.
# 2차원 배열에 연결되어있으면 mark: 인접행렬
# 대각선 기준으로 대칭 (전치해도 같은 값)
V, E = map(int, input().split())

arr = list(map(int, input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)]  # 인접행렬. 모든 엣지를 볼 수 있고 쉬움. 메모리 낭비 있음
adjL = [[] for _ in range(V+1)]  # 인접리스트: 각 숫자에 연결된 원소를 리스트에 담아 인덱스로 접근. 메모리 낭비 줄임
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]  # 간선정보를 두 개씩 끊어 읽어옴.
    adjM[v1][v2] = 1
    adjM[v2][v1] = 1

    adjL[v1].append(v2)
    adjL[v2].append(v1)
    