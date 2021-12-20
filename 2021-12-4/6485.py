# 6485. 삼성시의 버스 노선
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWczm7QaACgDFAWn

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())

    buses = list()
    for _ in range(N):
        buses.append(list(map(int, input().split())))

    P = int(input())
    stops = list()
    for _ in range(P):
        stops.append(int(input()))

    result = list()

    for stop in stops:
        bus_cnt = 0
        for start, end in buses:
            if start <= stop <= end:
                bus_cnt += 1
        result.append(bus_cnt)

    print(f'#{tc}', end=' ')
    print(*result)
