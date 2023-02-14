'''
<재귀 호출의 기본 구조>
def f(i, k):  # i for curruent status, k for the goal
    if i == k:  # 목표 도달
        return
    else:  
        f(i+1, k)  # 다음 단계
'''

# i번 원소를 복사하는 재귀함수
def f(i, k):
    if i == k:
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+i, k)


A = [10, 20, 30]
B = [0] * 3

f(0, 3)  # [10, 20, 30]