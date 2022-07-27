# 1208. [S/W 문제해결 기본] 1일차 - Flatten1208. [S/W 문제해결 기본] 1일차 - Flatten
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4

for tc in range(1, 11):
    n = int(input())
    brd = list(map(int, input().split()))

    for _ in range(n):
        topV = 0
        topIdx = 0
        minV = 101
        minIdx = 0
        for i in range(100):
            if brd[i] > topV:
                topV = brd[i]
                topIdx = i
            if brd[i] < minV:
                minV = brd[i]
                minIdx = i
        if minV == topV:
            break
        brd[topIdx] -= 1
        brd[minIdx] += 1
    print(f'#{tc} {max(brd) - min(brd)}')
