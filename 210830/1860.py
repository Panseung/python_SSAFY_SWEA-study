# 1860. 진기의 최고급 붕어빵
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LsaaqDzYDFAXc


def bread(M, K):
    cnt = 0
    maxT = max(lst)
    for i in range(0, maxT + 1):
        if i != 0 and i % M == 0:
            cnt += K
        if i == lst[0]:
            lst.pop(0)
            cnt -= 1
            if cnt < 0:
                return 'Impossible'
    return 'Possible'


TC = int(input())
for tc in range(1, TC + 1):
    N, M, K = map(int, input().split())  # N = 사람 수, M초 동안 K개의 붕어빵 제작
    lst = list(map(int, input().split()))
    lst.sort()
    print(f'#{tc} {bread(M, K)}')
