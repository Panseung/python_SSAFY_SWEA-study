# 13547. 팔씨름
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX6PP9G6p1sDFAS9&categoryId=AX6PP9G6p1sDFAS9&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

TC = int(input())
for tc in range(1, TC + 1):
    k = input()
    win = k.count('o')
    print(f'#{tc} ', end='')
    if 15 - len(k) >= 8 - win:
        print('YES')
    else:
        print('NO')
