# 1206. [S/W 문제해결 기본] 1일차 - View
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh

for tc in range(1, 11):
    length = int(input())
    buildings = list(map(int, input().split()))

    result = 0

    for i in range(2, length - 2):
        left1, left2 = buildings[i - 2], buildings[i - 1]
        building = buildings[i]
        right1, right2 = buildings[i + 1], buildings[i + 2]

        highest = max(left1, left2, right1, right2)

        if building > highest:
            result += building - highest

    print(f'#{tc} {result}')
