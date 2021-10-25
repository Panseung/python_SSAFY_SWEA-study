# 3499. 퍼펙트 셔플
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    lst = list(input().split())
    if len(lst) % 2 == 0:
        middle = N // 2
        print(f'#{tc}', end=' ')
        for i in range(middle):
            print(lst[i] + ' ' + lst[i + middle], end=' ')
        print()
    else:
        last = lst.pop(len(lst) // 2)
        middle = N // 2
        print(f'#{tc}', end=' ')
        for i in range(middle):
            print(lst[i] + ' ' + lst[i + middle], end=' ')
        print(last)
