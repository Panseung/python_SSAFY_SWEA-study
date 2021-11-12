# 1258. [S/W 문제해결 응용] 7일차 - 행렬찾기
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18LoAqItcCFAZN

def solve(y, x):
    global case_box, cnt
    if BRD[y][x] == 0 or visited[y][x] == 1:
        return

    else:
        visited[y][x] = 1
        x_len, y_len = 0, 0

        for dx in range(x, N):  # 현재 용기 x좌표 끝까지 가기
            if BRD[y][dx] == 0:
                break
            x_len += 1

        for dy in range(y, N):  # 현재 용기 y좌표 끝까지 가기
            if BRD[dy][x] == 0:
                break
            y_len += 1

        for vy in range(y, y + y_len):  # 방문표시
            for vx in range(x, x + x_len):
                visited[vy][vx] = 1

        case_box.append([x_len * y_len, y_len, x_len])
        cnt += 1
        return


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    BRD = []
    for _ in range(N):
        BRD.append(list(map(int, input().split())))

    cnt = 0
    visited = [[0] * N for _ in range(N)]
    case_box = []

    for y in range(N):
        for x in range(N):
            solve(y, x)

    case_box.sort()
    print(case_box)
    result = []
    while case_box:  # 정렬
        res_min = N ** 2
        pot = []
        del_idx = []
        for i in range(len(case_box)):
            if case_box[i][0] < res_min:  # 찾은 최솟값보다 더 작은 값 찾으면 다시 담기
                res_min = case_box[i][0]
                pot = []
                del_idx = []
                pot.append(case_box[i][1:])
                del_idx.append(i)
            elif case_box[i][0] == res_min:  # 최솟값이랑 같으면 어펜드하고 해당 번호 지우기
                pot.append(case_box[i][1:])
                del_idx.append(i)
        pot.sort()
        for i in pot:
            result.append(i)
        del_idx.sort(reverse=True)
        for i in del_idx:
            case_box.pop(i)

    print(f'#{tc} {cnt}', end=' ')
    for i in result:
        print(*i, end=' ')
    print()
