TC = int(input())
for tc in range(1, TC+1):
    N, Q = map(int, input().split())
    lst = []
    for q in range(Q):
        lst.append(list(map(int, input().split())))
    result = [0] * N
    for i in range(len(lst)):
        for j in range(lst[i][0], lst[i][1]+1):
            result[j-1] = i+1
    print(f'#{tc}', end=' ')
    print(*result)