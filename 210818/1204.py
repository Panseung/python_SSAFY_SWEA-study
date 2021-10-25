# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh


TC = int(input())
for tc in range(1, TC + 1):
    test_num = int(input())
    lst = list(map(int, input().split()))
    for i in range(len(lst) - 1):  # 리스트 오름차순 정렬
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    modeV = 1  # 최빈값 빈도수
    tmp = 1  # 현재 세고 있는 수의 빈도수
    pos = 0  # 반복문에 쓰일 현재 인덱스
    result = 0  # 최빈수
    while pos < 999:
        if lst[pos] == lst[pos + 1]:  # 현재 인덱스와 다음 인덱스의 수가 같을 때
            pos += 1  # 인덱스 +1
            tmp += 1  # 같으면 현재 수의 빈도수 +1
        else:
            if tmp > modeV:  # 현재 수의 빈도수가 최빈값의 빈도수보다 클 때
                result = lst[pos]
                modeV, tmp = tmp, 1  # 최빈값 업데이트, 현재 수의 빈도수 1로 초기화
                pos += 1  # 인덱스 +1
            elif tmp == modeV:  # 최빈값과 현재 수의 빈도수 같을 때
                if result > lst[pos]:  # 현재 수가 최빈값보다 크면 바꾸기
                    tmp = 1
                    pos += 1
                else:  # 그렇지 않으면 유지하기
                    result = lst[pos]
                    modeV, tmp = tmp, 1
                    pos += 1
            else:  # 현재 수와 다음 인덱스의 수가 다르고
                tmp = 1  # 현재 수의 빈도수가 최빈값의 빈도수보다 작으면
                pos += 1  # 인덱스 +1, 현재 수 빈도수 초기화
    print(f'#{tc} {result}')
