# 1979. 어디에 단어가 들어갈 수 있을까
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq

TC = int(input())
for tc in range(1, TC + 1):
    N, K = map(int, input().split())
    lst = list()
    cnt = 0
    for w in range(N):
        lst.append(list(map(int, input().split())))

    for w in range(N):
        for i in range(N - K + 1):
            if i == N - K:
                if 0 not in lst[w][i:i + K] and lst[w][i - 1] == 0:
                    cnt += 1
            elif i == 0:
                if 0 not in lst[w][i:i + K] and lst[w][i + K] == 0:
                    cnt += 1
            elif 0 not in lst[w][i:i + K] and lst[w][i + K] == 0 and lst[w][i - 1] == 0:
                cnt += 1

    for y in range(N):
        for x in range(N):
            if x > y:
                lst[x][y], lst[y][x] = lst[y][x], lst[x][y]

    for w in range(N):
        for i in range(N - K + 1):
            if i == N - K:
                if 0 not in lst[w][i:i + K] and lst[w][i - 1] == 0:
                    cnt += 1
            elif i == 0:
                if 0 not in lst[w][i:i + K] and lst[w][i + K] == 0:
                    cnt += 1
            elif 0 not in lst[w][i:i + K] and lst[w][i + K] == 0 and lst[w][i - 1] == 0:
                cnt += 1

    print(f'#{tc} {cnt}')


