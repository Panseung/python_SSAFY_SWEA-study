# 1974. 스도쿠 검증
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq


CT = int(input())
for ct in range(1, CT + 1):
    lst = []
    for i in range(9):
        lst.append(list(map(int, input().split())))

    result = 1
    for y in range(len(lst)):  # 가로
        box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in range(len(lst[y])):
            if lst[y][x] in box:
                box.remove(lst[y][x])
            else:
                result = 0
                break
    for y in range(len(lst)):  # 가로
        box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in range(len(lst[y])):
            if lst[x][y] in box:
                box.remove(lst[x][y])
            else:
                result = 0
                break
    y = 0
    x = 0
    XorY = 0
    while result == 1:

        if XorY == 9:
            break
        box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for dy in range(y, y + 3):
            for dx in range(x, x + 3):
                if lst[dy][dx] in box:
                    box.remove(lst[dy][dx])
                else:
                    result = 0
                    break
        XorY += 1
        if XorY % 3 == 0:
            x = 0
            y += 3
        else:
            x += 3

    print(f'#{ct} {result}')
