TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    BRD = [[0]*N for _ in range(N)]

    distance = N - 1
    pos_x = 0
    pos_y = 0
    num = 1
    while distance > 0:
        for i in range(pos_x, pos_x + distance):
            BRD[pos_y][i] = num
            num += 1
        pos_x += distance

        for i in range(pos_y, pos_y + distance):
            BRD[i][pos_x] = num
            num += 1
        pos_y += distance

        for i in range(pos_x, pos_x - distance, -1):
            BRD[pos_y][i] = num
            num += 1
        pos_x -= distance


        for i in range(pos_y, pos_y - distance, -1):
            BRD[i][pos_x] = num
            num += 1
        pos_y -= distance
        pos_x += 1
        pos_y += 1
        distance -= 2
    if N % 2 == 1:
        BRD[N//2][N//2] = N**2
    print(f'#{tc}')
    for i in BRD:
        print(*i)

