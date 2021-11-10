# 3347. 올림픽 종목 투표
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWDTHsZ6r0EDFAWD

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    costs = list(map(int, input().split()))
    judges = list(map(int, input().split()))

    votes = [0] * N

    for judge in range(M):
        for cost in range(N):
            if judges[judge] >= costs[cost]:
                votes[cost] += 1
                break

    result = votes.index(max(votes)) + 1

    print(f'#{tc} {result}')
