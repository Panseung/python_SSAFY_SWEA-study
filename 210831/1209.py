# 1209. [S/W 문제해결 기본] 2일차 - Sum
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh


TC = 10
for tc in range(1, TC + 1):
    test_num = input()
    BRD = []
    for _ in range(100):
        BRD.append(list(map(int, input().split())))
    result = 0  # 가로 최대
    for i in BRD:
        if sum(i) > result:
            result = sum(i)
    dia_R = 0  # 대각1 최대
    dia_L = 0  # 대각2 최대
    for i in range(100):
        dia_R += BRD[i][i]
        dia_L += BRD[i][99 - i]

    col = 0  # 세로 최대
    for y in range(100):
        pot = 0
        for x in range(100):
            pot += BRD[x][y]
        if pot > col:
            col = pot
    print(f'#{tc} {max([result, dia_L, dia_R, col])}')
