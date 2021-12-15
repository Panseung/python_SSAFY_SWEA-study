# 1221. [S/W 문제해결 기본] 5일차 - GNS
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14jJh6ACYCFAYD

TC = int(input())
for tc in range(TC):
    TC_num, N = input().split()
    lst = list(input().split())
    N = int(N)
    lst_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = []
    for j in range(len(lst_num)):
        for i in range(N):
            if lst[i] == lst_num[j]:
                result.append(lst[i])
    print(TC_num)
    print(*result)
