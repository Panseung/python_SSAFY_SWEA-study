CT = int(input())
for i in range(1, CT+1):
    N = int(input())
    lst = []
    pos = 0
    speed = 0
    for j in range(N):
        lst.append(list(map(int,input().split())))
    for j in range(len(lst)):
        if len(lst[j]) == 1:
            pos += speed
        elif lst[j][0] == 1:
            speed += lst[j][1]
            pos += speed
        else:
            speed -= lst[j][1]
            if speed < 0:
                speed = 0
            pos += speed

    print(f'#{i} {pos}')
