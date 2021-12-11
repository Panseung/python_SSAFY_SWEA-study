# 1209. [S/W 문제해결 기본] 2일차 - Sum
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh

for _ in range(1, 11):
    tc = int(input())
    result = 0
    BRD = []
    for _ in range(100):
        BRD.append(list(map(int, input().split())))

    for row in BRD:
        if sum(row) > result:
            result = sum(row)

    for x in range(100):
        col = 0
        for y in range(100):
            col += BRD[y][x]
        if col > result:
            result = col

    for i in range(100):
        cross = 0
        y, x = 99 - i, 0
        while 0 <= y <= 99 and 0 <= x <= 99:
            cross += BRD[y][x]
            y += 1
            x += 1
        if cross > result:
            result = cross

    for i in range(100):
        cross = 0
        y, x = 0, i
        while 0 <= y <= 99 and 0 <= x <= 99:
            cross += BRD[y][x]
            y += 1
            x -= 1
        if cross > result:
            result = cross

    print(f'#{tc} {result}')
