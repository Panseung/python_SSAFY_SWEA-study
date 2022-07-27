# 3499. 퍼펙트 셔플
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWGsRbk6AQIDFAVW&categoryId=AWGsRbk6AQIDFAVW&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    cards = list(input().split())
    print(f'#{tc} ', end='')
    for i in range(N):
        if i % 2:
            print(cards[(N + 1) // 2 + i // 2], end=' ')
        else:
            print(cards[i // 2], end=' ')
    print()
