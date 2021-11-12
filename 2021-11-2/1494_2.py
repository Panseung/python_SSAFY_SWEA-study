# 1494. 사랑의 카운슬러
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b_WPaAEIBBASw

def solve(k, sum_x, sum_y, res_x, res_y, state):  # 깊이, x합 , y합, 현재x, 현재y, 상태
    global result
    if k == N:
        sum_v = sum_x ** 2 + sum_y ** 2
        if result > sum_v:
            result = sum_v
        return

    elif result > sum_x ** 2 + sum_y ** 2:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                if state:  # 지금 지렁이 한마리가 선택된 상태면
                    x1 = res_x - worms[i][0]
                    # x2 = worms[i][0] - res_x
                    y1 = res_y - worms[i][1]
                    # y2 = worms[i][1] - res_y
                    solve(k + 1, sum_x + x1, sum_y + y1, 0, 0, 0)
                    # solve(k + 1, sum_x + x2, sum_y + y2, 0, 0, 0)
                else:
                    solve(k + 1, sum_x, sum_y, worms[i][0], worms[i][1], 1)
                visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    worms = []
    for _ in range(N):
        worms.append(list(map(int, input().split())))

    couple_cnt = N // 2  # 커플 수
    result = 10000000 ** 2 * N
    visited = [0] * N
    solve(0, 0, 0, 0, 0, 0)
    print(f'#{tc} {result}')
