# 4299. 태혁이의 사랑은 타이밍
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWLv6mx6htoDFAVV&categoryId=AWLv6mx6htoDFAVV&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6

TC = int(input())
for tc in range(1, TC + 1):
    d, h, m = map(int, input().split())
    result = 0
    result -= 60
    result -= 24 * 60 * 2
    d += 1
    h += 24
    m += 60
    result += m - 11
    result += (h - 11) * 60
    result += (d - 11) * 24 * 60
    if result < 0:
        result = -1
    print(f'#{tc} {result}')
