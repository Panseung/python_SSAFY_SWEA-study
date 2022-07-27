# 5515. 2016년 요일 맞추기
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWWOwecaFrIDFAV4&categoryId=AWWOwecaFrIDFAV4&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4

TC = int(input())
for tc in range(1, TC + 1):
    m, d = map(int, input().split())
    d += 3
    if m >= 2:
        d += 31
    if m >= 3:
        d += 29
    if m >= 4:
        d += 31
    if m >= 5:
        d += 30
    if m >= 6:
        d += 31
    if m >= 7:
        d += 30
    if m >= 8:
        d += 31
    if m >= 9:
        d += 31
    if m >= 10:
        d += 30
    if m >= 11:
        d += 31
    if m >= 12:
        d += 30
    d = d % 7
    print(f'#{tc} {d}')
