# 1238. [S/W 문제해결 기본] 10일차 - Contact
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD

from collections import deque

TC = 1
while TC <= 10:
    N, start = map(int, input().split())  # 데이터의 길이, 시작점
    graph = [[] for _ in range(101)]  # 그래프 리스트
    visited = [0] * 101  # 방문 여부 리스트
    visited[start] = 1  # 시작점 방문 체크하기
    lst = list(map(int, input().split()))

    for i in range(0, N, 2):  # 그래프 출발 지점인덱스에 갈 수 있는 번호 넣기
        from_num = lst[i]
        to_num = lst[i + 1]
        graph[from_num].append(to_num)

    queue = deque()
    queue.append([start, 1])

    result_box = []
    while queue:  # bfs로 접근
        res_num, turn = queue.popleft()
        for i in graph[res_num]:  # 갈 수 있는 지점중에
            if visited[i] == 0:  # 방문 안했으면
                visited[i] = 1  # 방문 했고
                queue.append([i, turn + 1])  # 큐에 넣어주고
                result_box.append([turn + 1, i])  # 숫자와 연락된 차례 넣어주기

    result_box.sort()  # 차례대로 정렬해서 가장 큰 값 호출하기

    print(f'#{TC} {result_box[-1][1]}')
    TC += 1

