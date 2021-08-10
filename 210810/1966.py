CT = int(input())
for q in range(1, CT+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N-1):
        for j in range(N-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(f'#{q}', end = ' ')
    print(*lst)
