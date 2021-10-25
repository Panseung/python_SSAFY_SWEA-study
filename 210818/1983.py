# 1983. 조교의 성적 매기기
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PwGK6AcIDFAUq


TC = int(input())
for tc in range(1, TC + 1):
    N, K = map(int, input().split())
    lst = []  # 학생 총점 리스트
    for _ in range(N):
        middle, final, assignment = map(int, input().split())
        lst.append(middle * 0.35 + final * 0.45 + assignment * 0.2)  # 합산점수로 바로 리스트 넣기
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grade_lst = []  # 줄 수 있는 등급 리스트(갯수 포함)
    for i in range(len(grade)):
        for j in range(N // 10):
            grade_lst.append(grade[i])
    higher = 0  # k번째 학생 보다 총점이 높은 사람 수
    for i in lst:
        if i > lst[K - 1]:
            higher += 1
    print(f'#{tc} {grade_lst[higher]}')
