# 1230. [S/W 문제해결 기본] 8일차 - 암호문3
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14zIwqAHwCFAYD&categoryId=AV14zIwqAHwCFAYD&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2

for tc in range(1):
    n = int(input())
    pw = list(map(int, input().split()))
    m = int(input())
    cmd = list(input().split())

    cnt = 0
    idx = 0
    for i in range(len(cmd)):
        if cmd[i] == '532' and cmd[i + 1] == '1':
            print(cmd[i:i+10])
            break
    print(f'#{tc}, {pw[0:10]}')


