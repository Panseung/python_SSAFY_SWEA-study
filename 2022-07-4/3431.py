# 3431. 준환이의 운동관리
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWE_ZXcqAAMDFAV2&categoryId=AWE_ZXcqAAMDFAV2&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

T = int(input())
for tc in range(1, T + 1):
    l, u, x = map(int, input().split())
    print(f'#{tc}', end=' ')
    if x < l:
        print(l - x)
    elif l <= x <= u:
        print(0)
    else:
        print(-1)
