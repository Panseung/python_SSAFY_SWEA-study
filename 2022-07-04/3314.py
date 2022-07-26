# 3314. 보충학습과 평균
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWBnA2jaxDsDFAWr&categoryId=AWBnA2jaxDsDFAWr&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2

TC = int(input())
for tc in range(1, TC + 1):
    lst = list(map(int, input().split()))
    sumV = 0
    for v in lst:
        sumV += max(40, v)
    print(f'#{tc} {sumV // len(lst)}')
