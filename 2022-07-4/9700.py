# 9700. USB 꽂기의 미스터리
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXDNEA3aaU0DFAVX&categoryId=AXDNEA3aaU0DFAVX&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=3

TC = int(input())
for tc in range(1, TC + 1):
    p, q = map(float, input().split())
    print(f'#{tc} ', end='')
    if (1 - p) * q < p * (1 - q) * q:
        print('YES')
    else:
        print('NO')
