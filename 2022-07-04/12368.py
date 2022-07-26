# 12368. 24시간
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXsEBlLqedsDFARX&categoryId=AXsEBlLqedsDFARX&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
TC = int(input())
for tc in range(1, TC + 1):
    a, b = map(int, input().split())
    print(f'#{tc}', end=' ')
    if a + b >= 24:
        print(a + b - 24)
    else:
        print(a + b)
