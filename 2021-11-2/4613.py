# 4613. 러시아 국기 같은 깃발
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQl9TIK8qoDFAXj

def solve1(ny, ncolor):
    plus_cnt = 0
    for i in range(M):
        if BRD[ny][i] != ncolor:
            plus_cnt += 1
    return plus_cnt


def solve(y, cnt, color):  # 몇째 줄, 바꾼 수, 현재 컬러
    global result
    if y == N - 1:
        if color != 'W':
            if result > cnt:
                result = cnt
        return

    elif color == 'W':
        solve(y + 1, cnt + solve1(y, 'W'), 'W')
        solve(y + 1, cnt + solve1(y, 'B'), 'B')

    elif color == 'B':
        solve(y + 1, cnt + solve1(y, 'B'), 'B')
        solve(y + 1, cnt + solve1(y, 'R'), 'R')

    else:
        solve(y + 1, cnt + solve1(y, 'R'), 'R')


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    BRD = []
    for _ in range(N):
        BRD.append(list(input()))

    base_cnt = 0

    for i in range(M):
        if BRD[0][i] != 'W':
            BRD[0][i] = 'W'
            base_cnt += 1
        if BRD[-1][i] != 'R':
            BRD[-1][i] = 'R'
            base_cnt += 1

    result = M * N
    solve(1, 0, 'W')
    print(f'#{tc} {result + base_cnt}')
