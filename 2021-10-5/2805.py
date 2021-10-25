TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    farm = []
    for _ in range(N):
        farm.append(input())

    result = []
    mid = N // 2  # 3
    for i in range(N // 2):
        result.append(farm[i][mid - i:mid + i + 1])
        result.append(farm[-1 - i][mid - i:mid + i + 1])

    result.append(farm[mid])
    sumV = 0
    for i in range(N):
        for j in result[i]:
            sumV += int(j)

    print(f'#{tc} {sumV}')
