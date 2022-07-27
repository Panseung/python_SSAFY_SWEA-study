# 1206. [S/W 문제해결 기본] 1일차 - View
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4

for tc in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    answer = 0
    for i in range(2, n - 2):
        sec = max(lst[i - 2], lst[i - 1], lst[i + 1], lst[i + 2])
        if lst[i] > sec:
            answer += lst[i] - sec

    print(f'#{tc} {answer}')
