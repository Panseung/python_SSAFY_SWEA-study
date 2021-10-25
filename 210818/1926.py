# 1926. 간단한 369게임
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq


N = int(input())
lst = []
result = []
for i in range(1, N + 1):
    lst.append(str(i))
for i in range(N):
    pot = ''
    cnt = 0
    for j in range(len(lst[i])):
        if lst[i][j] != '0' and int(lst[i][j]) % 3 == 0:
            pot += '-'
            cnt += 1
        else:
            pot += lst[i][j]
    if cnt > 0:
        pot = '-' * cnt
    result.append(pot)
print(*result)
