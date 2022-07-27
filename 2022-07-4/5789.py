# 5789. 현주의 상자 바꾸기
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWYygN36Qn8DFAVm&categoryId=AWYygN36Qn8DFAVm&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

TC = int(input())
for tc in range(1, TC + 1):
    n, q = map(int, input().split())
    lst = [0] * n
    for k in range(1, q + 1):
        l, r = map(int, input().split())
        for j in range(l - 1, r):
            lst[j] = k
    print(f'#{tc}', end=' ')
    print(*lst)
