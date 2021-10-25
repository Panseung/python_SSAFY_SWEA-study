T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    BRD = []
    for _ in range(N):
        BRD.append(list(input().split()))

    result_lst = [[] for _ in range(N)]
                                      # 1 2 3
    for i in range(N):  # 90도        # 4 5 6
        s = ''                        # 7 8 9
        for j in range(N):            # 7 4 1
            s += BRD[-1 - j][i]       # 8 5 2
        result_lst[i].append(s)       # 9 6 3

    for i in range(N):  # 180도
        s = ''
        for j in range(N):
            s += BRD[-1 - i][-1 - j]
        result_lst[i].append(s)

    for i in range(N):  # 270도
        s = ''
        for j in range(N):
            s += BRD[j][-1 - i]
        result_lst[i].append(s)

    print(f'#{tc}')
    for i in range(N):
        print(*result_lst[i])
