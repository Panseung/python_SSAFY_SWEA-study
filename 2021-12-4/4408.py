# 4408. 자기 방으로 돌아가기
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcJ2sapZMDFAV8

def my_space(num):
    num = int(num)
    return (num + 1) // 2


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    students = list()
    for _ in range(N):
        students.append(list(map(my_space, input().split())))

    corridor = [0] * 201
    for start, end in students:
        if start > end:
            start, end = end, start

        for i in range(start, end+1):
            corridor[i] += 1

    result_time = max(corridor)

    print(f'#{tc} {result_time}')
