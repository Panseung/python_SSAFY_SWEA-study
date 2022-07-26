# 10570. 제곱 팰린드롬 수
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXO72aaqPrcDFAXS&categoryId=AXO72aaqPrcDFAXS&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1


TC = int(input())
for tc in range(1, TC + 1):
    answer = 0
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        s = i ** 0.5
        if s == int(s):
            num = str(i)
            s = str(int(s))
            palindrome = True
            for j in range(len(num) // 2):
                if num[j] == num[-j - 1]:
                    continue
                else:
                    palindrome = False
                    break

            for j in range(len(s) // 2):
                if s[j] == s[-j - 1]:
                    continue
                else:
                    palindrome = False
                    break

            if palindrome:
                answer += 1
    print(f'#{tc} {answer}')
