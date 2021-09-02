TC = int(input())
for tc in range(1, TC+1):
    lst = list(map(int, input().split()))
    if lst[0] == lst[1] and lst[0] == lst[2]:
        print(f'#{tc} {lst[0]}')
    else:
        width = [lst[0]]
        height = []
        for i in range(1, 3):
            if lst[i] == width[0]:
                width.append(lst[i])
            else:
                height.append(lst[i])
        if len(width) == 2:
            print(f'#{tc} {height[0]}')
        else:
            print(f'#{tc} {width[0]}')