# 1221. 5432. 쇠막대기 자르기
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl47b6DGMDFAXm

TC = int(input())
for tc in range(1, TC + 1):
    case = input()

    pos = 0  # 현재 계산 위치
    res_bars = 0  # 현재까지 놓여있는 잘릴 막대기 갯수
    result = 0  # 출력할 잘린 막대기 갯수들
    while pos < len(case):
        if case[pos] == '(':
            if case[pos+1] == ')':
                result += res_bars
                pos += 2
            else:
                result += 1
                res_bars += 1
                pos += 1
        else:
            res_bars -= 1
            pos += 1

    print(f'#{tc} {result}')

