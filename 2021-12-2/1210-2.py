# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh

dy = [0, 0, -1]
dx = [-1, 1, 0]


def ladder(res_x, res_y):
    global result
    if res_y == 0:
        result = res_x
        return

    else:
        for d in range(3):
            new_y = res_y + dy[d]
            new_x = res_x + dx[d]
            if 0 <= new_x < 100 and not visited[new_y][new_x] and BRD[new_y][new_x]:
                visited[new_y][new_x] = 1
                ladder(new_x, new_y)
                break


for _ in range(10):
    tc = int(input())
    BRD = list()
    for _ in range(100):
        BRD.append(list(map(int, input().split())))

    start_x = 0
    for x_pos in range(100):
        if BRD[99][x_pos] == 2:
            start_x = x_pos

    result = 0
    visited = [[0] * 100 for _ in range(100)]
    visited[99][start_x] = 1
    ladder(start_x, 99)

    print(f'#{tc} {result}')
