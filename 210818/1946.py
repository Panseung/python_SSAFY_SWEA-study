# 1946. 간단한 압축 풀기
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PmkDKAOMDFAUq


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    lst = []
    original = ''
    for n in range(N):
        lst.append(input().split())
        lst[n][1] = int(lst[n][1])
        original += lst[n][0] * lst[n][1]
    lst = []
    print(f'#{tc}')
    for n in range(len(original) // 10 + 1):
        print((original[n * 10:(n + 1) * 10]))
