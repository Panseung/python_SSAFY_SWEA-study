# 14178. 1차원 정원
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX_N3oSqcyUDFARi&categoryId=AX_N3oSqcyUDFARi&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

TC = int(input())
for tc in range(1, TC + 1):
    n, d = map(int, input().split())
    length = 2 * d + 1
    result = n / (2 * d + 1)
    if result % 1:
        result += 1
    result = int(result)
    print(f'#{tc} {result}')
