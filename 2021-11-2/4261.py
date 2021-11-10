# 4261. 빠른 휴대전화 키패드
# Level D4
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWLL7kaaAPsDFAUW

alpha_lst = [0, 0, ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
             ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

TC = int(input())
for tc in range(1, TC + 1):
    S, N = input().split()
    lst = list(input().split())

    length = len(S)

    word_lst = []
    for i in lst:
        if len(i) == length:
            word_lst.append(i)

    result = 0

    for j in word_lst:
        test = True
        for k in range(length):
            if j[k] not in alpha_lst[int(S[k])]:
                test = False
                break
        if test:
            result += 1

    print(f'#{tc} {result}')
