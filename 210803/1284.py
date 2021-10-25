# 1284. 수도 요금 경쟁
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV189xUaI8UCFAZN


cnt = int(input())
for i in range(cnt):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    B = Q + (W - R) * S
    if (W - R) < 0:
        if A > Q:
            print(f'#{i + 1} {Q}')
        else:
            print(f'#{i + 1} {A}')
    else:
        if A > B:
            print(f'#{i + 1} {B}')
        else:
            print(f'#{i + 1} {A}')
