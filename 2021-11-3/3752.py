# 3752. 가능한 시험 점수
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWHPkqBqAEsDFAUn


def make_score(k, sum_score):
    if k == N:
        visited[sum_score] = 1
        return
    else:
        make_score(k+1, sum_score + scores[k])
        make_score(k+1, sum_score)


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    scores = list(map(int, input().split()))

    max_score = sum(scores)
    visited = [0] * (max_score + 1)
    make_score(0, 0)

    cnt = 0
    for i in range(max_score + 1):
        if visited[i]:
            cnt += 1
    print(f'#{tc} {cnt}')
