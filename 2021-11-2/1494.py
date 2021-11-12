# 1494. 사랑의 카운슬러
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b_WPaAEIBBASw

def solve(k, lst):
    global result
    if k == N:
        sum_x = 0
        sum_y = 0
        for worm1, worm2 in lst:
            sum_x += worm1[0] - worm2[0]
            sum_y += worm1[1] - worm2[1]
        sum_v = sum_x ** 2 + sum_y ** 2
        if result > sum_v:
            result = sum_v
            print(lst[:])
        return

    else:
        for i in range(couple_cnt):
            if len(lst[i]) < 2:
                lst[i].append(worms[k])
                solve(k + 1, lst)
                lst[i].remove(worms[k])
            else:
                worm1 = lst[i][0]
                worm2 = lst[i][1]
                x = worm1[0] - worm2[0]
                y = worm1[1] - worm2[1]
                if result <= x ** 2 + y ** 2:
                    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    worms = []
    for _ in range(N):
        worms.append(list(map(int, input().split())))

    couple_cnt = N // 2  # 커플 수
    lst = [[] for _ in range(couple_cnt)]
    result = 10000000 ** 2 * N
    solve(0, lst)
    print(f'#{tc} {result}')
