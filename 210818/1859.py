def wonjae(lst):
    day = 0
    sell_price = max(lst)
    items = 0
    paying = 0
    earning = 0
    while day < len(lst):
        if lst[day] < sell_price:       #오늘이 가장 비싼날이 아니면 구입
            paying += lst[day]
            items += 1
            day += 1
        elif lst[day] == sell_price:    #오늘이 가장 비싼날이면 판매
            earning += lst[day]*items - paying
            paying = 0
            items = 0
            sell_price = 0
            day += 1
            for i in range(day, len(lst)):  # 새로운 가장 비싼 날 찾기
                if lst[i] > sell_price:
                    sell_price = lst[i]
    return earning

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f'#{tc} {wonjae(lst)}')