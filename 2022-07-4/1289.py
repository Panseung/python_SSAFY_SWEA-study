# 1289. 원재의 메모리 복구하기
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV19AcoKI9sCFAZN&categoryId=AV19AcoKI9sCFAZN&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

TC = int(input())
for tc in range(1, TC + 1):
    m = input()
    idx = 0
    cnt = 0
    res = 0
    while idx < len(m):
        if int(m[idx]) != res:
            cnt += 1
            res = (res + 1) % 2
        idx += 1
    print(f'#{tc} {cnt}')
