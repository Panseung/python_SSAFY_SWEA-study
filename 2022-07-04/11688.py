# 11688. Calkin-Wilf tree 1
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXgZSOn6ApIDFASW&categoryId=AXgZSOn6ApIDFASW&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2

TC = int(input())
for tc in range(1, TC + 1):
    S = input()
    l, r = 1, 1
    for s in S:
        if s == 'L':
            r += l
        else:
            l += r
    print(f'#{tc} {l} {r}')
