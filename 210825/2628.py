def cutting(square, direction_point):
     y1 = square[0]
     x1 = square[1]
     y2 = square[2]
     x2 = square[3]
     direction = direction_point[0]
     point = direction_point[1]
     if direction:  # 세로이면
         if x1 < point < x2:
             return [y1, x1, y2, point, y1, point, y2, x2]
     else:
         if y1 < point < y2:
             return [y1, x1, point, x2, point, x1, y2, x2]
     return square


width, height = map(int, input().split())
N = int(input())
cutting_lst = []
square_lst = [[0, 0, height, width]]
for n in range(N):
    cutting_lst.append(list(map(int, input().split())))

for i in cutting_lst:
    for j in square_lst:
        square_lst.pop(0)
        pieces = cutting(j, i)
        if len(pieces) > 4:
            square_lst.append(pieces[0:4])
            square_lst.append(pieces[4:8])
        else:
            square_lst.append(pieces)
print(square_lst)




