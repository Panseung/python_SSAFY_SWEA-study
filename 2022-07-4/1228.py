# 1228. [S/W 문제해결 기본] 8일차 - 암호문1
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14w-rKAHACFAYD&categoryId=AV14w-rKAHACFAYD&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=3

for tc in range(10):
    n = int(input())
    pw = list(map(int, input().split()))
    m = int(input())
    cmd = list(input().split())
    cmd.append('t')

    cnt = 0
    idx = 0
    while cnt < m:
        res_cmd = cmd[idx]
        idx += 1
        if res_cmd == 'D':
            for i in range(int(cmd[idx + 1])):
                if idx + 1 >= len(pw):
                    break
                del pw[int(cmd[idx])]
            idx += 2
        else:
            pos, num = int(cmd[idx]), int(cmd[idx + 1])
            idx += 2
            for i in range(num):
                pw.insert(pos + i, cmd[idx])
                idx += 1
        cnt += 1
    answer = pw[0:10]
    print(f'#{tc + 1}', end=' ')
    print(*answer)
