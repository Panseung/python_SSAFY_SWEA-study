# link
# https://www.acmicpc.net/status?user_id=jodie9596&problem_id=14501&from_mine=1


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
    lst.append([a, b])
result = 0
solve(0, 0)
print(result)
