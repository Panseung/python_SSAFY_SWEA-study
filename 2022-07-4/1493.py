# 1493. 수의 새로운 연산
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV2b-QGqADMBBASw&categoryId=AV2b-QGqADMBBASw&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6

def solve(num):
    v = 1
    y = 1
    x = 1
    while v < num:
        x += 1
        y -= 1
        if y == 0:
            y = x
            x = 1
        v += 1
    return [y, x]


TC = int(input())
for tc in range(1, TC + 1):
    p, q = map(int, input().split())
    y1, x1 = solve(p)
    y2, x2 = solve(q)
    y = y1 + y2
    x = x1 + x2

    nx, ny, nv = 1, 1, 1
    while True:
        nv += 1
        ny -= 1
        nx += 1
        if ny == 0:
            ny = nx
            nx = 1

        if ny == y and nx == x:
            print(f'#{tc} {nv}')
            break
