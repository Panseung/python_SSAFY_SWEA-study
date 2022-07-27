# 2806. N-Queen
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GKs06AU0DFAXB&categoryId=AV7GKs06AU0DFAXB&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6

def chess(lst, l):
    global answer
    if len(lst) == l:
        answer += 1
        # print(lst)
        return
        # print('---------------')
    ry = len(lst)
    for rx in range(l):
        pas = True
        for y, x in lst:
            if rx == x or abs(ry - y) == abs(rx - x):
                pas = False
                break
        if pas:
            tmp = lst[::]
            tmp.append([ry, rx])
            chess(tmp, l)


TC = int(input())
for tc in range(1, TC + 1):
    n = int(input())
    answer = 0
    for i in range(n):
        visited = [[0] * n for _ in range(n)]
        chess([[0, i]], n)
    print(f'#{tc} {answer}')
