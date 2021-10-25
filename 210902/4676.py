# 4676. 늘어지는 소리 만들기
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWRKWITqfvIDFAV8


TC = int(input())
for tc in range(1, TC + 1):
    S = input()
    lst = []
    for i in S:
        lst.append(i)

    H = int(input())
    H_lst = list(map(int, input().split()))
    H_lst.sort(reverse=True)
    for i in H_lst:
        lst.insert(i, '-')

    result = ''
    for i in lst:
        result += i
    print(f'#{tc} {result}')
