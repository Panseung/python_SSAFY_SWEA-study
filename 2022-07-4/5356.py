# 5356. 의석이의 세로로 말해요
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWVWgkP6sQ0DFAUO&categoryId=AWVWgkP6sQ0DFAUO&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

TC = int(input())
for tc in range(1, TC + 1):
    result = ''
    lst = [input() for _ in range(5)]
    for x in range(15):
        for y in range(5):
            if len(lst[y]) > x:
                result += lst[y][x]
    print(f'#{tc} {result}')
