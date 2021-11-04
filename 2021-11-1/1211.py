# 1211. [S/W 문제해결 기본] 2일차 - Ladder2
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14BgD6AEECFAYh


def maze(start):
    pos_y = 0
    pos_x = start
    distance = 0
    visited = [[0] * 100 for _ in range(100)]
    while pos_y < 99:
        visited[pos_y][pos_x] = 1
        if pos_x - 1 >= 0 and BRD[pos_y][pos_x - 1] == 1 and not visited[pos_y][pos_x - 1]:  # 왼쪽 길 있으면
            pos_x -= 1
        elif pos_x + 1 < 100 and BRD[pos_y][pos_x + 1] == 1 and not visited[pos_y][pos_x + 1]:  # 오른쪽 길 있으면
            pos_x += 1
        else:  # 밑으로 가야하면
            pos_y += 1
        distance += 1  # 어디로 가든 거리는 늘어나니 마지막에 distance + 1
    return distance


for tc in range(1, 11):
    input()
    BRD = []
    for i in range(100):
        BRD.append(list(map(int, input().split())))
    start_lst = []  # 스타트 지점 담는 리스트
    for x in range(100):  # 스타트 지점 찾기
        if BRD[0][x] == 1:
            start_lst.append(x)

    result_pos = 0
    result_value = 10000

    for i in start_lst:
        if result_value > maze(i):
            result_value = maze(i)
            result_pos = i
    print(f'#{tc} {result_pos}')
