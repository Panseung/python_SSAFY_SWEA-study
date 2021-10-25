# 5603. [Professional] 건초더미
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXGEbd6cjMDFAUo


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(int(input()))
    avg = sum(lst) // N
    result = 0
    for i in range(N):
        result += abs(avg - lst[i])
    print(f'#{tc} {int(result * 0.5)}')
