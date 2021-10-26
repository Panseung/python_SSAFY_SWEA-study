# 4963. 섬의 개수
# Level Silver 2
# Link : https://www.acmicpc.net/problem/4963

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, 1, -1]

while True:  
    w, h = map(int, input().split())
    if w == 0 and h == 0:  # 입력 끝나면 종료 조건 표시
        break

    BRD = []
    for _ in range(h):
        BRD.append(list(input().split()))

    visited = [[0] * w for _ in range(h)]
    cnt = 0

    for y in range(h):
        for x in range(w):
            if BRD[y][x] == '1' and visited[y][x] == 0:
                visited[y][x] = 1
                stack = [[y, x]]
                
                while stack:  # 스택
                    ny, nx = stack.pop()
                    for i in range(8):
                        new_y = ny + dy[i]
                        new_x = nx + dx[i]
                        if 0 <= new_y < h and 0 <= new_x < w:
                            if BRD[new_y][new_x] == '1' and visited[new_y][new_x] == 0:
                                visited[new_y][new_x] = 1
                                stack.append([new_y, new_x])
                cnt += 1

    print(cnt)
