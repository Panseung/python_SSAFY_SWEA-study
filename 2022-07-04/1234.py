# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14_DEKAJcCFAYD&categoryId=AV14_DEKAJcCFAYD&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2

for tc in range(1, 11):
    L, S = input().split()

    while True:
        ing = False
        for i in range(len(S) - 1):
            if S[i] == S[i + 1]:
                ing = True
                s1 = S[0:i]
                s2 = S[i+2: len(S)]
                S = s1 + s2
                break
        if not ing:
            break

    print(f'#{tc} {S}')
