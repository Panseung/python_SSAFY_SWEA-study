# 6109. 추억의 2048게임
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWbrg9uabZsDFAWQ

def solve_up(row, col):
    if row == N-1:
        return

    else:
        if BRD[row][col] == 0:
            for i in range(col, N-1):
                BRD[i][col] = BRD[i+1][col]
            BRD[N-1][col] = 0
            solve_up(row+1, col)
        elif BRD[row][col] == BRD[row+1][col]:
            BRD[row][col] *= 2
            BRD[row+1][col] = 0
            solve_up(row+1, col)
        else:
            solve_up(row+1, col)


def solve_down(row, col):


TC = int(input())
for tc in range(1, TC+1):
    N, S = input().split()
    N = int(N)
    BRD = []
    for _ in range(N):
        BRD.append(list(map(int, input().split())))

    # dy, dx = 0, 0
    # if S == 'up':
    #     dy, dx = -1, 0
    # elif S == 'down':
    #     dy, dx = 1, 0
    # elif S == 'left':
    #     dy, dx = 0, -1
    # else:
    #     dy, dx = 1, 0

