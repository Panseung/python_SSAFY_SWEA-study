# 1984. 중간 평균값 구하기
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pw_-KAdcDFAUq


def my_max(lst):  # max 함수
    MaxV = 0
    for i in range(len(lst)):
        if lst[i] > MaxV:
            MaxV = lst[i]
    return MaxV


def my_min(lst):  # min 함수
    MinV = lst[0]
    for i in range(len(lst)):
        if lst[i] < MinV:
            MinV = lst[i]
    return MinV


def my_sum(lst):  # sum 함수
    result = 0
    for i in range(len(lst)):
        result += lst[i]
    return result


TC = int(input())  # 문제풀이
for tc in range(1, TC + 1):
    lst = list(map(int, input().split()))
    lst.remove(my_min(lst))
    lst.remove(my_max(lst))
    meanV = my_sum(lst) // len(lst)
    if (my_sum(lst) / len(lst)) - meanV >= 0.5:
        meanV += 1
    print(f'#{tc} {meanV}')
