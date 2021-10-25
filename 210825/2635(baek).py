# 2635. 수 이어가기
# 백준
# Link : https://www.acmicpc.net/problem/2635

def connecting(lst):
    global N
    M = 1
    maxV = 0
    result = []
    while M <= N:
        lst.append(M)
        while lst[-2] >= lst[-1]:
            lst.append(lst[-2] - lst[-1])
        if len(lst) > maxV:
            maxV = len(lst)
            result = lst[:]
        M += 1
        lst = [N]
    return [maxV, result]


N = int(input())
lst = [N]
print(connecting(lst)[0])
print(*connecting(lst)[1])
