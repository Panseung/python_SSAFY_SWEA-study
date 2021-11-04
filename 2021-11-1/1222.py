# 1222. [S/W 문제해결 기본] 6일차 - 계산기1
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14mbSaAEwCFAYD

for tc in range(1, 11):
    N = int(input())
    s = input()
    result = 0
    for i in range(0, N, 2):
        result += int(s[i])
    print(f'#{tc} {result}')