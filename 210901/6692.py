TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    box = []
    for n in range(N):
        box.append(list(map(float, input().split())))
    result = 0
    for a, b in box:
        result += a*b
    print(f'#{tc} {result}')