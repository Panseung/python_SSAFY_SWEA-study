TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    students = list(range(1, N+1))
    result = []
    for i in students:
        if i not in lst:
            result.append(i)
    print(f'#{tc}', end=' ')
    print(*result)