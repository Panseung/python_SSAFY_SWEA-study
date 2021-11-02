# 1868. 파핑파핑 지뢰찾기
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LwsHaD1MDFAXc

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, 1, -1]


def mine(y, x, click, n):
    global result

    if x == N - 1:
        next_y = y + 1
        next_x = 0
    else:
        next_y = y
        next_x = x + 1

    if n == N * N:  # 끝가지 확인했으면!
        result = click
        return click

    elif visited[y][x] or BRD[y][x] == '*':  # 방문 했거나 지뢰면
        mine(next_y, next_x, click, n + 1)

    else:  # 방문 안했고 현재 위치가 지뢰가 아니면!
        visited[y][x] = 1
        stack = [[y, x]]
        while stack:
            res_y, res_x = stack.pop()
            res_0 = True

            for i in range(8):  # 현재 지점이 0인지 체크하기
                ny = res_y + dy[i]
                nx = res_x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    if BRD[ny][nx] == '*':
                        res_0 = False

            for i in range(8):
                ny = res_y + dy[i]
                nx = res_x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    if BRD[ny][nx] == '*':
                        res_0 = False
                    elif BRD[ny][nx] == '.':
                        is_mine = False
                        for j in range(8):  # 인접한 부분이 0이면 스택에 넣기
                            sec_y = ny + dy[j]
                            sec_x = nx + dx[j]
                            if 0 <= sec_y < N and 0 <= sec_x < N and BRD[sec_y][sec_x] == '*':
                                is_mine = True
                                break
                        if not is_mine:
                            stack.append([ny, nx])
                            visited[ny][nx] = 1  # 범위 안이고, 지뢰 없고, 방문 안했으면 방문 체크

        mine(next_y, next_x, click + 1, n + 1)


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    BRD = []
    for _ in range(N):
        BRD.append(input())

    result = 0
    visited = [[0] * N for _ in range(N)]
    mine(0, 0, 0, 0)
    print(result)
