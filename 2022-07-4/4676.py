# 4676. 늘어지는 소리 만들기
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWRKWITqfvIDFAV8&categoryId=AWRKWITqfvIDFAV8&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

TC = int(input())
for tc in range(1, TC + 1):
    s = input()
    h = int(input())
    lst = list(map(int, input().split()))
    cnt = [0] * 21
    for l in lst:
        cnt[l] += 1
    result = ''
    for i in range(len(s)):
        if cnt[i]:
            result += '-' * cnt[i]
        result += s[i]
    result += '-' * cnt[len(s)]
    print(f'#{tc} {result}')
