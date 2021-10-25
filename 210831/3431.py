# 3431. 준환이의 운동관리
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWE_ZXcqAAMDFAV2


TC = int(input())
for tc in range(1, TC + 1):
    L, U, X = map(int, input().split())
    print(f'#{tc}', end=' ')
    if X < L:
        print(L - X)
    elif L <= X <= U:
        print(0)
    else:
        print(-1)
