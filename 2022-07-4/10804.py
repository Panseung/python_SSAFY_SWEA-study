# 10804. 문자열의 거울상
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXTC0x16D8EDFASe&categoryId=AXTC0x16D8EDFASe&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=3

TC = int(input())
for tc in range(1, TC + 1):
    S = input()
    S = S[::-1]
    answer = ''
    for s in S:
        if s == 'b':
            answer += 'd'
        elif s == 'd':
            answer += 'b'
        elif s == 'p':
            answer += 'q'
        else:
            answer += 'p'
    print(f'#{tc} {answer}')
