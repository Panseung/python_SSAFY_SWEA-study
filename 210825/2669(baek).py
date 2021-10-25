# 2669. 직사각형 네개의 합집합의 면적 구하기
# 백준
# Link : https://www.acmicpc.net/problem/2669


def square(lst):
    x1 = lst[0]
    y1 = lst[1]
    x2 = lst[2]
    y2 = lst[3]
    for y in range(y1, y2):
        for x in range(x1, x2):
            if [y, x, y + 1, x + 1] not in box:
                box.append([y, x, y + 1, x + 1])
    return len(box)


pot = []
for n in range(4):
    pot.append(list(map(int, input().split())))
box = []
for n in range(4):
    square(pot[n])
print(len(box))
