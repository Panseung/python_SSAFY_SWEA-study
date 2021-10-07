def burgerking(k, score, kcal):
    global result, lst
    if k == N:
        if kcal < L:
            lst.append(score)
            return
    else:
        burgerking(k+1, score, kcal)
        burgerking(k+1, score + burger_lst[k][0], kcal + burger_lst[k][1])



T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    burger_lst = []
    for _ in range(N):
        burger_lst.append(list(map(int, input().split())))
    lst = []
    burgerking(0, 0, 0)
    result = max(lst)
    print(f'#{tc} {result}')