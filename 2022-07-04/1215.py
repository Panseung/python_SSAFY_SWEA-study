# 1215. [S/W 문제해결 기본] 3일차 - 회문1
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14QpAaAAwCFAYi&categoryId=AV14QpAaAAwCFAYi&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
def solve(sy, sx, length, wh):
    global answer
    result = ''
    if wh == 'w':
        for i in range(length):
            result += brd[sy][sx + i]
    else:
        for i in range(length):
            result += brd[sy + i][sx]
    yes = True
    for j in range(length // 2):
        if result[j] == result[-1 - j]:
            continue
        yes = False
        break
    if yes:
        answer += 1
    return


for tc in range(1, 11):
    answer = 0
    l = int(input())
    brd = [input() for _ in range(8)]
    for y in range(8):
        for x in range(9 - l):
            solve(y, x, l, 'w')
    for y in range(9 - l):
        for x in range(8):
            solve(y, x, l, 'h')
    print(f'#{tc} {answer}')
