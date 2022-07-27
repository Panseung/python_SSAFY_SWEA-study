# 10912. 외로운 문자
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXVJuEvqLAADFASe&categoryId=AXVJuEvqLAADFASe&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

TC = int(input())
for tc in range(1, TC + 1):
    S = input()
    alpha = []
    for s in S:
        alpha.append(s)
    alpha = list(set(alpha))
    result = []
    for a in alpha:
        if S.count(a) % 2:
            result.append(a)
    result.sort()
    answer = ''
    for r in result:
        answer += r
    if answer == '':
        print(f'#{tc} Good')
    else:
        print(f'#{tc} {answer}')
