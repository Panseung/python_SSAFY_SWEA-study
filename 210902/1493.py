def new_cal(num):
    pos = [1, 1]
    cnt = 1
    sum_pos = 2
    while cnt < num:
        if pos[1] == 1:
            pos[0] = 1
            pos[1] = sum_pos
            sum_pos += 1
        else:
            pos[0] += 1
            pos[1] -= 1
        cnt += 1
    return pos


def new_cal_reverse(lst):
    pos = [1, 1]
    cnt = 1
    sum_pos = 2
    while pos != lst:
        if pos[1] == 1:
            pos[0] = 1
            pos[1] = sum_pos
            sum_pos += 1
        else:
            pos[0] += 1
            pos[1] -= 1
        cnt += 1
    return cnt


TC = int(input())
for tc in range(1, TC+1):
    p, q = map(int, input().split())
    p = new_cal(p)
    q = new_cal(q)
    result = [p[0]+q[0], p[1]+q[1]]
    print(f'#{tc} {new_cal_reverse(result)}')
