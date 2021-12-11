# 1208. [S/W 문제해결 기본] 1일차 - Flatten
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh


def top(BRD):
    maxV = 0
    pos = 0
    for i in range(len(BRD)):
        if BRD[i] > maxV:
            maxV = BRD[i]
            pos = i
    return maxV, pos


def bottom(BRD):
    minV = BRD[0]
    pos = 0
    for i in range(len(BRD)):
        if BRD[i] < minV:
            minV = BRD[i]
            pos = i
    return minV, pos


def dump(BRD, cnt):
    while cnt > 0:
        TV, TP = top(BRD)
        BV, BP = bottom(BRD)
        BRD[TP] -= 1
        BRD[BP] += 1
        cnt -= 1
    TV, TP = top(BRD)
    BV, BP = bottom(BRD)
    return TV - BV


TC = 10
for tc in range(1, TC + 1):
    cnt = int(input())
    BRD = list(map(int, input().split()))
    print(f'#{tc} {dump(BRD, cnt)}')
