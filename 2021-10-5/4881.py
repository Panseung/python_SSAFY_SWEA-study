def solve(y, n):  # y : 재귀 횟수이자 y축, n은 합
    global result
    if y == N:  # 재귀 종료 조건
        if n < result:  # 기존 결과값보다 작으면 업데이트하기
            result = n
        return
    elif n < result:  # 백트래킹
        for i in range(N):
            if visited[i] == 0:  # 방문 안했으면
                visited[i] = 1  # 방문체크하고
                solve(y + 1, n + BRD[y][i])  # 재귀 들어가기
                visited[i] = 0  # 재귀 나오면 방문여부 다시 풀기

#  2 1 2
#  5 8 5
#  7 2 2
# [1 0 1]


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    BRD = []  # 보드 판
    for _ in range(N):  # 보드판에 입력값 입력하기
        BRD.append(list(map(int, input().split())))
    result = 9 * N  # 최대로 초기값 설정하기
    visited = [0] * N  # visited 방문여부 리스트
    solve(0, 0)  # 함수
    print(f'#{tc} {result}')
