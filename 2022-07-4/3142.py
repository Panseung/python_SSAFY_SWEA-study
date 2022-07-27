# 3142. 영준이와 신비한 뿔의 숲
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV_6xWk6sbADFAWS&categoryId=AV_6xWk6sbADFAWS&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4

TC = int(input())
for tc in range(1, TC + 1):
    n, m = map(int, input().split())
    r1 = m * 2 - n
    r2 = m - r1
    print(f'#{tc} {r1} {r2}')
