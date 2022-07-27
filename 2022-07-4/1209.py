# 1209. [S/W 문제해결 기본] 2일차 - Sum
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=3


for _ in range(10):
    tc = int(input())
    brd = [list(map(int, input().split())) for _ in range(100)]
    answer = 0

    for y in range(100):
        sumV = sum(brd[y])
        if sumV > answer:
            answer = sumV

    for x in range(100):
        sumV = 0
        for y in range(100):
            sumV += brd[y][x]
        if sumV > answer:
            answer = sumV

    sumV1 = 0
    sumV2 = 0
    for i in range(100):
        sumV1 += brd[i][i]
        sumV2 += brd[99 - i][i]

    print(f'#{tc} {max(answer, sumV1, sumV2)}')
