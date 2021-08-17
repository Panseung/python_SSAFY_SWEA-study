TC=int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    BRD = []
    for i in range(N):
        BRD.append(list(map(int, input().split())))
    result = 0  #가장 많이 잡은 파리 수
    for y in range(N-M+1):
        for x in range(N-M+1):
            sum_fly = 0 #반복문에 따라 잡은 파리 수
            for dy in range(M):
                for dx in range(M):
                    sum_fly += BRD[y+dy][x+dx]
            if sum_fly > result:
                result = sum_fly
    print(f'#{tc} {result}')