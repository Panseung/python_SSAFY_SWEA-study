# 1208. [S/W 문제해결 기본] 1일차 - Flatten
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh

def dump():
    highest = max(boxes)
    lowest = min(boxes)
    highest_change = False
    lowest_change = False
    for i in range(100):
        if highest_change and lowest_change:
            break
        elif boxes[i] == highest and not highest_change:
            boxes[i] -= 1
            highest_change = True
        elif boxes[i] == lowest and not lowest_change:
            boxes[i] += 1
            lowest_change = True


for tc in range(1, 11):
    dump_cnt = int(input())
    boxes = list(map(int, input().split()))
    for i in range(dump_cnt):
        dump()

    result = max(boxes) - min(boxes)

    print(f'#{tc} {result}')
