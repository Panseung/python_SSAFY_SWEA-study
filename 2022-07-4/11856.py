# 11856. 반반
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXjS1GXqZ8gDFATi&categoryId=AXjS1GXqZ8gDFATi&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4

TC = int(input())
for tc in range(1, TC + 1):
    S = input()
    my_set = []
    for s in S:
        my_set.append(s)
    my_set = list(set(my_set))
    print(f'#{tc} ', end='')
    if S.count(S[0]) == len(S) // 2 and len(my_set) == 2:
        print('Yes')
    else:
        print('No')
