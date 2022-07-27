# 6692. 다솔이의 월급 상자
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWdXofhKFkADFAWn&categoryId=AWdXofhKFkADFAWn&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4

TC = int(input())
for tc in range(1, TC + 1):
    n = int(input())
    answer = 0
    for _ in range(n):
        a, b = map(float, input().split())
        answer += a * b
    print(f'#{tc} {round(answer, 6)}')
