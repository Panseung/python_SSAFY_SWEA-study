# 1970. 쉬운 거스름돈
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PsIl6AXIDFAUq


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f'#{tc}')
    for money in lst:
        if money == 10:
            print(N // money)
        else:
            print(N // money, end=' ')
        N = N % money
