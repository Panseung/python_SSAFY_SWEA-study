# 1218. [S/W 문제해결 기본] 4일차 - 괄호 짝짓기
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14eWb6AAkCFAYD

for tc in range(1, 11):
    N = int(input())
    s = input()

    stack = []

    for i in s:
        if i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                break

        elif i == ']':
            if stack[-1] == '[':
                stack.pop()

        elif i == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                break

        elif i == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                break
        else:
            stack.append(i)
    if stack:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
