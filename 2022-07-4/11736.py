# 11736. 평범한 숫자
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXhh-H-KwUcDFARQ&categoryId=AXhh-H-KwUcDFARQ&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

TC = int(input())
for tc in range(1, TC + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    answer = 0
    for i in range(1, n - 1):
        v = lst[i]
        minV = min(lst[i - 1:i + 2])
        maxV = max(lst[i - 1:i + 2])
        if minV < v < maxV:
            answer += 1
    print(f'#{tc} {answer}')
