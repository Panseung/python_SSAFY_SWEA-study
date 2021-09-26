def diagonal1(y, x):
    while y > 0 and x > 0:
        y -= 1
        x -= 1
    while y < N or x < N:
        BRD[y][x] = 1
        y += 1
        x += 1


def diagonal2(y, x):
    while y < N and x > 0:
        y += 1
        x -= 1
    while y > 0 or x < N:
        BRD[y][x] = 1
        y -= 1
        x += 1


def cross(y, x):
    for k in range(N):
        BRD[y][k] = 1
        BRD[k][x] = 1


def test_diagonal1(y, x):
    while y > 0 and x > 0:
        y -= 1
        x -= 1
    while y < N or x < N:
        if BRD[y][x] == 1:
            return False
        y += 1
        x += 1
    return True


def test_diagonal2(y, x):
    while y < N and x > 0:
        y += 1
        x -= 1
    while y > 0 or x < N:
        if BRD[y][x] == 1:
            return False
        y -= 1
        x += 1
    return True


def test_cross(y, x):
    for q in range(N):
        if BRD[y][q] == 1 or BRD[q][x] == 1:
            return False
    return True


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    BRD = [[0]*N for _ in range(N)]
    cnt = 0  # 경우의 수
    Q_cnt = 0  # 퀸의 수
    for i in range(N):
        dy, dx = 0, i
        Q_cnt += 1
        diagonal1(dy, dx)
        diagonal2(dy, dx)
        cross(dy, dx)
        dy, dx = 1, 0
        while dy < N:
            if test_cross(dy, dx) and test_diagonal1(dy, dx) and test_diagonal2(dy, dx):
                cross(dy, dx)
                diagonal1(dy, dx)
                diagonal2(dy, dx)
                dy += 1
                dx = 0
                Q_cnt += 1
            else:
                dx += 1
                if dx == N:
                    break
        if Q_cnt == N:
            cnt += 1
        BRD = [[0] * N for _ in range(N)]
    print(cnt)
