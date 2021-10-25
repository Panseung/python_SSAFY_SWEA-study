# 1229. [S/W 문제해결 기본] 8일차 - 암호문2
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14yIsqAHYCFAYD


TC = 10
for tc in range(1, TC + 1):
    N = int(input())
    origin = list(map(int, input().split()))
    cnt = int(input())
    cmd = list(input().split())
    for i in range(len(cmd)):
        if cmd[i] == 'I':
            x = int(cmd[i + 1])
            y = int(cmd[i + 2])
            for j in range(y):
                origin.insert(x, cmd[i + 2 + y - j])
        elif cmd[i] == 'D':
            x = int(cmd[i + 1])
            y = int(cmd[i + 2])
            for j in range(y):
                del origin[x]
    print(f'#{tc}', end=' ')
    print(*origin[0:10])
