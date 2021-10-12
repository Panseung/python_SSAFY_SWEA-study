def longest(n, d, cur):
    global result, please
    if n == N-1:
        if d > result:
            result = d
    elif N-n+d > result:
        k = n+1
        for i in range(n+1, N):
            if lst[i] > cur:
                k = i
                break
        if lst[k] > cur:
            longest(k, d, cur)
            longest(k, d+1, lst[k])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    result = 0
    please = ''
    longest(-1, 0, 0)
    print(f'#{tc} {result}')