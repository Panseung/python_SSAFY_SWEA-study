TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    result = 0
    for k in range(1, K+1):
        result += lst[-k]
    print(f'#{tc} {result}')