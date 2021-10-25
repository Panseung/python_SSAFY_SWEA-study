# 9700. USB 꽂기의 미스터리
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXDNEA3aaU0DFAVX


TC = int(input())
for tc in range(1, TC + 1):
    p, q = map(float, input().split())
    s1 = (1 - p) * q
    s2 = p * (1 - q) * q
    if s2 > s1:
        result = 'YES'
    else:
        result = 'NO'
    print(f'#{tc} {result}')
