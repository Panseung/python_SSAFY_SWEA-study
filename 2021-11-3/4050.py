# 4050. 재관이의 대량 할인
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIseXoKEUcDFAWN

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    prices.sort(reverse=True)

    result = sum(prices)

    for i in range(2, N, 3):
        result -= prices[i]

    print(f'#{tc} {result}')
