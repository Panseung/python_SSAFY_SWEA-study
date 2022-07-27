# 5431. 민석이의 과제 체크하기
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWVl3rWKDBYDFAXm&categoryId=AWVl3rWKDBYDFAXm&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=3

TC = int(input())
for tc in range(1, TC + 1):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    check = [0] * 101
    for s in lst:
        check[s] = 1
    print(f'#{tc} ', end='')
    for i in range(1, n + 1):
        if not check[i]:
            print(i, end=' ')
    print()
