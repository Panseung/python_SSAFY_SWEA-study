# 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14dUIaAAUCFAYD&categoryId=AV14dUIaAAUCFAYD&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

def solve(val, res, k, e):
    global result
    if k == e:
        result = res
        return
    else:
        solve(val, res * val, k + 1, e)


for _ in range(10):
    tc = int(input())
    a, b = map(int, input().split())
    result = 0
    solve(a, a, 1, b)
    print(f'#{tc} {result}')
