# 10200. 구독자 전쟁
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXMCXV_qVgkDFAWv&categoryId=AXMCXV_qVgkDFAWv&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4

TC = int(input())
for tc in range(1, TC + 1):
    n, a, b = map(int, input().split())

    minV = min(a, b)
    maxV = max(a + b - n, 0)
    print(f'#{tc} {minV} {maxV}')
