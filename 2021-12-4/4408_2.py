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

    result_time = 0

    while students:
        result_time += 1

        using_space = []
        escape_students = []
        for i in range(len(students)):
            my_start = min(students[i])
            my_end = max(students[i])

            test = True

            for start, end in using_space:
                if my_end < start or my_start > end:
                    continue
                else:
                    test = False
                    break

            if test:
                using_space.append([my_start, my_end])
                escape_students.append(i)

        escape_students.sort(reverse=True)

        for student_number in escape_students:
            students.pop(student_number)

    print(f'#{tc} {result_time}')

