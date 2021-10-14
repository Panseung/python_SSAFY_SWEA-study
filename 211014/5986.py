def solve(n, sumV, k):
    global cnt
    if n == 3:
        if sumV == N:
            cnt += 1
        return
    elif sumV < N:
        for i in prime_lst:
            if i <= k:
                solve(n + 1, sumV + i, i)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(range(N))
    lst_TF = [True] * N
    lst_TF[0] = False
    lst_TF[1] = False
    pos = 2
    prime_lst = []
    while pos < N:
        prime_lst.append(pos)
        for i in range(pos, len(lst), pos):
            lst_TF[i] = False
        for i in range(pos, len(lst)):
            if lst_TF[i] == True:
                next_pos = i
                break
        if next_pos == pos:
            break
        else:
            pos = next_pos
    cnt = 0
    solve(0, 0, prime_lst[-1])
    print(f'#{tc} {cnt}')