# 3456. 직사각형 길이 찾기
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWFPmsqqALwDFAV0&categoryId=AWFPmsqqALwDFAV0&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=3

TC = int(input())
for tc in range(1, TC + 1):
    a, b, c = map(int, input().split())
    print(f'#{tc} ', end='')
    if a == b and a == c:
        print(a)
    else:
        if a == b:
            print(c)
        elif a == c:
            print(b)
        else:
            print(a)
