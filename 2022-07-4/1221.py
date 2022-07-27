# 1221. [S/W 문제해결 기본] 5일차 - GNS
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14jJh6ACYCFAYD&categoryId=AV14jJh6ACYCFAYD&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

TC = int(input())
nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for _ in range(TC):
    tc, l = input().split()
    lst = list(input().split())
    result = []
    for i in range(10):
        for _ in range(lst.count(nums[i])):
            result.append(nums[i])
    print(tc)
    print(*result)
