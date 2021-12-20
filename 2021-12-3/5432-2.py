# 1221. 5432. 쇠막대기 자르기
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl47b6DGMDFAXm

TC = int(input())
for tc in range(1, TC + 1):
    case = input()

    stack = []
    pos = 0
    result = 0
    while pos < len(case):
        if case[pos] == '(':
            if case[pos + 1] == ')':
                result += len(stack)
                pos += 2
            else:
                result += 1
                stack.append('(')
                pos += 1
        else:
            stack.pop()
            pos += 1

    print(f'#{tc} {result}')
