TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    P_lst = list(map(int, input().split()))
    cnt = 0
    for i in range(1, len(P_lst)-1):
        normal = P_lst[i]
        left = P_lst[i-1]
        right = P_lst[i+1]
        pot = [normal, right, left]
        if max(pot) != normal and min(pot) != normal:
            cnt += 1
    print(f'#{tc} {cnt}')