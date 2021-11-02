# 1227. [S/W 문제해결 기본] 7일차 - 미로2
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14wL9KAGkCFAYD

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(10):
    tc = int(input())
    BRD = []
    for i in range(100):
        BRD.append(input())

    start_y, start_x = 0, 0
    for y in range(1, 99):
        check = False
        for x in range(1, 99):
            if BRD[y][x] == '3':
                start_y = y
                start_x = x
                check = True
                break
        if check:
            break

    result = 0
    queue = deque()
    visited = [[0] * 100 for _ in range(100)]
    queue.append([start_y, start_x])
    while queue:
        y, x = queue.popleft()
        escape = False
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 1 <= ny < 99 and 1 <= nx < 99 and visited[ny][nx] == 0:
                if BRD[ny][nx] == '2':
                    escape = True
                    result = 1
                    break
                elif BRD[ny][nx] == '0':
                    visited[ny][nx] = 1
                    queue.append([ny, nx])
        if escape:
            break
    print(f'#{tc} {result}')
