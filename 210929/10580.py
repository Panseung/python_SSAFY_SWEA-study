TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    line = []
    for _ in range(N):
        line.append(list(map(int, input().split())))

    line.sort(key = lambda x:x[0])

    cross = 0
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            if line[i][0] < line[j][0] and line[i][1] > line[j][1]:
                cross += 1

    print(f'#{tc} {cross}')