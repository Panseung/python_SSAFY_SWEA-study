dy = [-1, 1, 0, 0, -1, -1, 1, 1]  # 상하좌우 대각
dx = [0, 0, -1, 1, -1, 1, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    BRD = [[0] * N for _ in range(N)]

    mid = N // 2  # 배열 중간에 기본으로 있는 백돌, 흑돌 놔두는 작업
    BRD[mid][mid] = 2
    BRD[mid - 1][mid - 1] = 2
    BRD[mid][mid - 1] = 1
    BRD[mid - 1][mid] = 1

    for _ in range(M):
        x, y, c = map(int, input().split())
        y = y - 1  # 인덱스로 인해 y, x 각 -1씩 해주기
        x = x - 1
        BRD[y][x] = c  # 돌 놓은곳 위치 바꿔주기
        for i in range(8):  # 상하좌우대각 모두 진행하기
            if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N:  # 한칸씩 이동한 새로운 좌표가 범위안에 들어오면
                new_y = y + dy[i]
                new_x = x + dx[i]
                distance = 0  # 색을 바꿔줄 돌의 수
                while 0 <= new_y < N and 0 <= new_x < N:  # 범위안에 존재하면
                    if BRD[new_y][new_x] == 3 - c:  # 놔둔 돌의 옆 돌이 자신과 반대되는 색이라면
                        new_y += dy[i]  # 해당 좌표로 옮기고
                        new_x += dx[i]
                        distance += 1  # 색 바꿔줄 돌의 수 +1
                    elif BRD[new_y][new_x] == c:  # 만약 같은 색이라면
                        for j in range(distance):  # distance 만큼 작업 진행하기
                            BRD[new_y - dy[i] * (1 + j)][new_x - dx[i] * (1 + j)] = c
                        break
                    else:  # 0이 나오면 아무 일도 하지않고 끝내기  0 1 2 2 2 2 0
                        break

    white_cnt = 0  # 흑,백 돌 카운팅
    black_cnt = 0
    for i in range(N):
        for j in range(N):
            if BRD[i][j] == 1:
                black_cnt += 1
    white_cnt = M + 4 - black_cnt  # 흰 돌 : 기본 돌 4개 + 놔둔 돌의수 - 검은 돌 수

    print(f'#{tc} {black_cnt} {white_cnt}')
