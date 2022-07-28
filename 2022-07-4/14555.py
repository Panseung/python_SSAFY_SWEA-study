# 14555. 공과 잡초
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYGtoa3qARcDFARC&categoryId=AYGtoa3qARcDFARC&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

TC = int(input())
for tc in range(1, TC + 1):
    s = input()
    idx = 0
    answer = 0
    while idx < len(s):
        if s[idx] == '(':
            answer += 1
            idx += 1
        elif s[idx] == ')':
            answer += 1
        idx += 1
    print(f'#{tc} {answer}')
