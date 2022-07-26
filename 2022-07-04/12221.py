# 12221. 구구단2
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXpz3dravpQDFATi&categoryId=AXpz3dravpQDFATi&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2

TC = int(input())
for tc in range(1, TC + 1):
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {a * b}')
