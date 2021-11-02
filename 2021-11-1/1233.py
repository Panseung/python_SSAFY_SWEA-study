# 1233. [S/W 문제해결 기본] 9일차 - 사칙연산 유효성 검사
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141176AIwCFAYD

for tc in range(1, 11):
    N = int(input())
    operators = ['+', '-', '*', '/']
    result = 1  # 출력될 결과의 초깃값
    line = 1  # 마지막 줄 4
    while True:
        res = 2 ** line - 1
        if res < N:
            line += 1
        else:
            break

    last_num_cnt = N - 2 ** (line - 1) + 1  # 마지막 줄에 있는 노드의 수 2
    if last_num_cnt % 2 == 0:  # 마지막 줄에 있는 노드의 수가 짝수면! (짝수여야함)
        only_num_pos = N - (2 ** (line - 2) + last_num_cnt // 2)
        # 숫자가 들어가야 하는 노드의 수는 마지막 줄 위의 노드 수 + 마지막 줄의 노드수 / 2
        # 따라서 숫자가 나오기 시작하는 인덱스는 전체 N - 숫자 들어가는 노드의 수

        for i in range(N):  # 숫자가 나와야 하는 지점부터 숫자가 나오면 결과 안바뀜
            s = list(input().split())  # 입력 받기
            num_or_op = s[1]
            if i < only_num_pos:
                if num_or_op not in operators:  # operator 나와야 하는데 숫자나오면 result = 0
                    result = 0
            else:
                if num_or_op in operators:  # 숫자 나와야 하는데 operator 나오면 result = 0
                    result = 0
    else:  # 마지막 줄에 있는 노드 수가 짝수가 아니면 계산이 안됨
        result = 0
        for i in range(N):
            input()  # 입력 받기
    print(f'#{tc} {result}')
