def per(k, sumv):
    global minv
    if sumv >= minv: #합이 기존 minv보다 커지면 중단
        return

    if k == n: # 끝까지 다 오면
        if minv > sumv: # minv를 구함
            minv = sumv
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                t[k] = i
                per(k+1, sumv + lst[k][i])
                visited[i] = False

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    t = [-1] * n
    visited = [False] * n
    minv = 10 * n
    per(0, 0)
    print('#{} {}'.format(tc, minv))