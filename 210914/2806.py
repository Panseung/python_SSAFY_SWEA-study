# 2806. N-Queen
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB


def check(y, x):
    global cnt
    if y == N:
        cnt += 1
        return cnt
    else:
        ly = ry = y
        lx = rx = x
        while ly > 0 and lx > 0:  # 대각선1 시작점 찾기
            lx -= 1
            ly -= 1
        while rx + 1 < N and ry > 0:  # 대각선2 시작점 찾기
            rx += 1
            ry -= 1

        for i in range(N):
            if N > lx and lx >= 0 and N > ly and ly >= 0:
                if BRD[ly][lx] == 0:
                    lx += 1
                    ly += 1
                else:
                    return False
            if N > rx and rx >= 0 and N > ry and ry >= 0:
                if BRD[ry][rx] == 0:
                    rx -= 1
                    ry += 1
                else:
                    return False
            if BRD[y][i] != 0:
                return False
            if BRD[i][x] != 0:
                return False
        return True


def chess(row):
    global cnt
    if row == N:
        cnt += 1
        return
    else:
        for i in range(N):
            if check(row, i):
                BRD[row][i] = 1
                chess(row + 1)
                BRD[row][i] = 0
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    BRD = [[0] * N for _ in range(N)]
    cnt = 0

    print(f'#{tc} {chess(0)}')
