# 2628. 종이자르기
# 백준
# Link : https://www.acmicpc.net/problem/2628


def cutting(square, direction_point):
    y1 = square[0]
    x1 = square[1]
    y2 = square[2]
    x2 = square[3]
    direction = direction_point[0]
    point = direction_point[1]
    new_square = []
    if direction:  # 세로이면
        if x1 < point < x2:
            new_square.append([y1, x1, y2, point])
            new_square.append([y1, point, y2, x2])
    else:
        if y1 < point < y2:
            new_square.append([y1, x1, point, x2])
            new_square.append([point, x1, y2, x2])
    if new_square:
        return new_square
    else:
        return square


width, height = map(int, input().split())
N = int(input())
cutting_lst = []
square_lst = [[0, 0, height, width]]
for n in range(N):
    cutting_lst.append(list(map(int, input().split())))
for i in cutting_lst:
    pieces_lst = []
    for j in square_lst:
        pieces = cutting(j, i)
        if len(pieces) == 2:
            for p in pieces:
                pieces_lst.append(p)
        else:
            pieces_lst.append(pieces)
    square_lst = pieces_lst[:]

result = 0
for i in square_lst:
    tmp = (i[2] - i[0]) * (i[3] - i[1])
    if tmp > result:
        result = tmp
print(result)
