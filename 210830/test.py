N = int(input())
lst = [[] for _ in range(N)]
house = []
base = []
for n in range(N):
    x = 0
    for i in input():
        lst[n].append(i)
        if i == 'H':
            house.append([n, x])
        elif i != 'X':
            base.append([n, x, i])
        x += 1
cnt = len(house)
for i in range(len(house)):
    for j in base:
        if j[2] == 'A':
            distance = 1
        elif j[2] == 'B':
            distance = 2
        elif j[2] == 'C':
            distance = 3
        if house[i][1] == j[1] and abs(house[i][0] - j[0]) <= distance:
            lst[house[i][0]][house[i][1]] = 'X'
        elif house[i][0] == j[0] and abs(house[i][1] - j[1]) <= distance:
            lst[house[i][0]][house[i][1]] = 'X'
result = 0
for y in range(N):
    for x in range(N):
        if lst[y][x] == 'H':
            result += 1
print(result)