def part_sum(k, sumV):
    global cnt
    if k == N:
        if sumV == K:
            cnt += 1
    else:
        if sumV + lst[k] <= K:
            part_sum(k+1, sumV + lst[k])
        part_sum(k+1, sumV)


TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    part_sum(0, 0)
    print(f'#{tc} {cnt}')