# 10505. 소득 불균형
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXNP4CvauaMDFAXS&categoryId=AXNP4CvauaMDFAXS&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

TC = int(input())
for tc in range(1, TC + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    even = sum(lst) // n
    answer = 0
    for l in lst:
        if l <= even:
            answer += 1
    print(f'#{tc} {answer}')
