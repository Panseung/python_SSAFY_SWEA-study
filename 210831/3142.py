# 3142. 영준이와 신비한 뿔의 숲
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_6xWk6sbADFAWS


TC = int(input())
for tc in range(1, TC + 1):
    n, m = map(int, input().split())
    twin = n - m
    uni = m - twin
    print(f'#{tc} {uni} {twin}')
