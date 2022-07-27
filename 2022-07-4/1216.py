# 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=3

for _ in range(10):
    tc = int(input())
    brd = [input() for _ in range(100)]
    answer = 1
    for length in range(99, 0, - 1):
        f1 = False
        for y in range(99):
            f2 = False
            for x in range(99):
                if x + length <= 100:
                    right = True
                    for k in range(length // 2):
                        if brd[y][x + k] != brd[y][x + length - 1 - k]:
                            right = False
                            break
                    if right:
                        answer = length
                        f1, f2 = True, True
                        break
            if f2:
                break
        if f1:
            break

    for length in range(99, answer, - 1):
        f1 = False
        for x in range(99):
            f2 = False
            for y in range(99):
                if y + length <= 100:
                    right = True
                    for k in range(length // 2):
                        if brd[y + k][x] != brd[y + length - 1 - k][x]:
                            right = False
                            break
                    if right:
                        answer = length
                        f1, f2 = True, True
                        break
            if f2:
                break
        if f1:
            break

    print(f'#{tc} {answer}')
