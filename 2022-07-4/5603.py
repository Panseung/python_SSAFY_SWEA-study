# 5603. [Professional] 건초더미
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWXGEbd6cjMDFAUo&categoryId=AWXGEbd6cjMDFAUo&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

TC = int(input())
for tc in range(1, TC + 1):
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    mean = sum(lst) // n
    result = 0
    for v in lst:
        if v > mean:
            result += v - mean
    print(f'#{tc} {result}')
