dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
tank = ['^', 'v', '<', '>']

def find_direc(cy, cx):
    if game_map[cy][cx] == '^':
        return 0
    elif game_map[cy][cx] == 'v':
        return 1
    elif game_map[cy][cx] == '<':
        return 2
    else:
        return 3


def shoot(posy, posx, direction):
    meet_wall = True
    while meet_wall:
        posy += dy[direction]
        posx += dx[direction]
        if posy < 0 or posy >= H or posx < 0 or posx >= W:    # 포탄이 맵 밖으로 나가면
            break
            
        elif game_map[posy][posx] == '#':
            meet_wall = False
        elif game_map[posy][posx] == '*':
            game_map[posy][posx] = '.'
            meet_wall = False


def move(posy, posx, direction):
    global pos_y, pos_x
    shape = '^'
    for i in range(4):
        if direction == i:
            posy += dy[i]
            posx += dx[i]
            shape = tank[i]
            break
    if posy < 0 or posy >= H or posx < 0 or posx >= W:
        return
    elif game_map[posy][posx] == '.': # 평지면 탱크위치 옮겨주기
        game_map[pos_y][pos_x] = '.' # 탱크있던자리에 잔디 깔아주기
        pos_y += dy[i]
        pos_x += dx[i]
        game_map[pos_y][pos_x] = shape



T = int(input())
for t in range(1, T+1):
    H, W = map(int, input().split())
    game_map = [[] for _ in range(H)]
    for i in range(H):
        line = input()
        for j in line:
            game_map[i] += j

    cmd_len = int(input())
    S = input()
    cmd_lst = []
    for i in S:
        cmd_lst.append(i)

    pos_y = 0           # 게임 시작시 전차 위치 찾기
    pos_x = 0
    tank = ['<', '>', '^', 'v']         # 질문!!!!!!!!!!!!
    for y in range(H):
        for x in range(W):
            if game_map[y][x] in tank:
                pos_y, pos_x = y, x
                break

    direc = find_direc(pos_y, pos_x)
    while cmd_lst:
        cmd = cmd_lst.pop(0)
        if cmd == 'S':
            shoot(pos_y, pos_x, direc)
        else:
            if cmd == 'U':
                game_map[pos_y][pos_x] = '^'
                direc = 0
            elif cmd == 'D':
                game_map[pos_y][pos_x] = 'v'
                direc = 1
            elif cmd == 'L':
                game_map[pos_y][pos_x] = '<'
                direc = 2
            elif cmd == 'R':
                game_map[pos_y][pos_x] = '>'
                direc = 3
            move(pos_y, pos_x, direc)

    result = [''] * H
    for i in range(H):
        for j in range(W):
            result[i] += game_map[i][j]

    print(f'#{t}', end = ' ')
    for i in range(H):
        print(result[i])

