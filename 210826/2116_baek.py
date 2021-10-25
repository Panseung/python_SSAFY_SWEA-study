# 2116. 주사위 쌓기
# 백준
# Link : https://www.acmicpc.net/problem/2116


def top_bottom(i):
    if i == 0:
        return 5
    if i == 1:
        return 3
    if i == 2:
        return 4
    if i == 3:
        return 1
    if i == 4:
        return 2
    if i == 5:
        return 0


cnt = int(input())
dice_box = []
for _ in range(cnt):
    dice_box.append(list(map(int, input().split())))
result = []
for i in range(6):
    case = 0
    bottom = i
    top = top_bottom(i)
    for j in range(cnt):
        pot = []
        for d in range(6):
            if d != bottom and d != top:
                pot.append(dice_box[j][d])
            if d == top:
                bottom_num = dice_box[j][d]
        case += max(pot)
        if j + 1 < cnt:
            for k in range(6):
                if dice_box[j + 1][k] == bottom_num:
                    bottom = k
                    top = top_bottom(k)
                    break
    result.append(case)

print(max(result))
