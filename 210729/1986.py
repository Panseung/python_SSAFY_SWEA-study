# 1986. 지그재그 숫자
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PxmBqAe8DFAUq

cnt = int(input())  # 시행횟수 첫줄 입력

for i in range(cnt):
    lst = []
    a = int(input())
    for j in range(1, a + 1):
        lst.append(j)
    plus = (lst[::2])
    minus = (lst[1::2])
    print(f'#{i + 1} {sum(plus) - sum(minus)}')
