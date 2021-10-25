# 5515. 2016년 요일 맞추기
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWWOwecaFrIDFAV4


TC = int(input())
for tc in range(1, TC + 1):
    m, d = map(int, input().split())
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    cnt = d
    if m >= 2:
        for i in range(m - 1):
            cnt += day[i]
    result = (cnt + 3) % 7
    print(f'#{tc} {result}')
