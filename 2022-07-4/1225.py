# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

from collections import deque

for _ in range(10):
    tc = int(input())
    pw = list(map(int, input().split()))
    m = min(pw)
    cnt = m % 30
    m -= cnt
    for i in range(8):
        pw[i] -= m
    pw = deque(pw)
    minV = 1
    while True:
        res = pw.popleft()
        res -= minV
        minV = minV % 5 + 1
        pw.append(res)
        if pw[-1] <= 0:
            pw[-1] = 0
            break

    print(f'#{tc} ', end='')
    print(*pw)
