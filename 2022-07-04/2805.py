# 2805. 농작물 수확하기
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2

TC = int(input())
for tc in range(1, TC + 1):
    answer = 0
    n = int(input())
    lst = []
    for i in range(n):
        S = input()
        tmp = []
        for j in range(len(S)):
            tmp.append(int(S[j]))
        lst.append(tmp)

    for y in range(n):
        answer += sum(lst[y])

    for y in range(n // 2):
        for x in range(n // 2):
            if y + x < n // 2:
                answer -= lst[y][x]
                answer -= lst[n - 1 - y][x]
                answer -= lst[y][n - 1 - x]
                answer -= lst[n - 1 - y][n - 1 - x]

    print(f'#{tc} {answer}')
