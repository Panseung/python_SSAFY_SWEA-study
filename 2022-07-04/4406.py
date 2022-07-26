# 4406. 모음이 보이지 않는 사람
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWNcD_66pUEDFAV8&categoryId=AWNcD_66pUEDFAV8&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
vowels = ['a', 'e', 'i', 'o', 'u']
TC = int(input())
for tc in range(1, TC + 1):
    S = input()
    result = ''
    for s in S:
        if s in vowels:
            continue
        result += s
    print(f'#{tc} {result}')
