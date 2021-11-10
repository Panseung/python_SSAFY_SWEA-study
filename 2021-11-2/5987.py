# 5987. 달리기
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWaJ4g86WA4DFAUQ
def solve(order, k):
    global result
    if k == N:
        for winner, loser in case:
            if order.index(winner) > order.index(loser):
                result -= 1
                break
        return
    else:
        for i in range(1, N + 1):
            if visited[i] == 0:
                visited[i] = 1
                solve(order + str(i), k + 1)
                visited[i] = 0


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    case = []
    for _ in range(M):
        case.append(list(input().split()))

    result = 1
    for i in range(1, N + 1):
        result *= i

    visited = [0] * (N + 1)
    solve('', 0)

    print(result)
