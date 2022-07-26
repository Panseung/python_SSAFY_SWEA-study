# 1220. [S/W 문제해결 기본] 5일차 - Magnetic
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2


for tc in range(1, 11):
    input()
    brd = [list(map(int, input().split())) for _ in range(100)]
    answer = 0
    for y in range(100):
        for x in range(100):
            if brd[y][x] == 1:
                for i in range(y + 1, 100):
                    if brd[i][x] == 2:
                        answer += 1
                        break
                    elif brd[i][x] == 1:
                        break
    print(f'#{tc} {answer}')
