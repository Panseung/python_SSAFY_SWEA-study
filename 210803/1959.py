# 1959. 두 개의 숫자열
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq


cnt = int(input())
for k in range(cnt):
    Ai, Bj = map(int, input().split())
    A = []
    B = []
    q = 0
    lst = []
    A += map(int, input().split())
    B += map(int, input().split())
    if Ai <= Bj:
        for i in range(abs(Bj - Ai) + 1):
            result = []
            for j in range(len(A)):
                result.append(A[j] * B[j + q])
            lst.append(sum(result))
            q += 1
        print(f'#{k + 1} {max(lst)}')
    else:
        for i in range(abs(Ai - Bj) + 1):
            result = []
            for j in range(len(B)):
                result.append(A[j + q] * B[j])
            lst.append(sum(result))
            q += 1
        print(f'#{k + 1} {max(lst)}')
