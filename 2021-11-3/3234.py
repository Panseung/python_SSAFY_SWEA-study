# 3234. 준환이의 양팔저울
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWAe7XSKfUUDFAUw

def solve(k, left, right):
    global cnt
    if right > left:
        return
    elif k == N:
        print(left, right)
        cnt += 1
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                solve(k + 1, left, right + weights[k])
                solve(k + 1, left + weights[k], right)
                visited[i] = 0


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    visited = [0] * N
    cnt = 0
    solve(0, 0, 0)
    print(f'#{tc} {cnt}')
