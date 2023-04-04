"""
# input.in
5 8 : 마지막 정점 번호, 간선 수
0 1 2  : 시작 노드, 끝 노드, 가중치
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
"""

def dijkstra(s, V):
    U = [0] * (V+1)  # 최소비용이 결정된 정점 집합, like 'visited'
    U[s] = 1
    for i in range(V+1):  # 시작점과 각 노드와의 거리를 업데이트
        D[i] = adjM[s][i]

    for _ in range(V):  # 시작점을 제외한 모든 노드에 대해.
        minV = inf
        w = 0
        for i in range(V+1):
            if not U[i] and minV > D[i]:  # 아직 방문하지 않았고, 거리가 더 가까우면.
                w = i
                minV = D[i]
        U[w] = 1  # 방문 기록 남기기
        for v in range(V+1):
            if 0 < adjM[w][v] < inf:  # 자기자신이 아니고, 접근 가능하면.
                D[v] = min(D[v], D[w]+adjM[w][v])


inf = 10000  # 임의의 큰 값
V, E = map(int, input().split())
adjM = [[inf] * (V+1) for _ in range(V+1)]  # 큰 값으로 초기화 한 인접 행렬
for i in range(V+1):
    adjM[i][i] = 0  # 자기자신 = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w

D = [0] * (V+1)  # 해당 인덱스까지의 최단 거리를 담을 배열
dijkstra(0, V)  # 시작점, 마지막 노드 번호
print(D)
