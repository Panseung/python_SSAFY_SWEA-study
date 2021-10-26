# 14501. 퇴사
# Level Silver 3
# link : https://www.acmicpc.net/problem/14501


def solve(n, pot):
    global result
    if n >= N:
        if n == N:
            if pot > result:
                result = pot
            return
        return
    else:
        solve(n + lst[n][0], pot + lst[n][1])
        solve(n + 1, pot)


N = int(input())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])  # a : 걸리는 날짜 b : 금액
result = 0
solve(0, 0)
print(result)
