# 2005. 파스칼의 삼각형
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    pascal = []
    for i in range(N):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:  # row의 맨 첫부분 or 끝 부분일 때는 1 넣어주기
                row.append(1)
            else:
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        pascal.append(row)
    print(f'#{tc}')
    for i in range(N):
        print(*pascal[i])
