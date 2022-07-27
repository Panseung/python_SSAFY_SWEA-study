# 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=3
pw = {'0': '0001101',
      '1': '0011001',
      '2': '0010011',
      '3': '0111101',
      '4': '0100011',
      '5': '0110001',
      '6': '0101111',
      '7': '0111011',
      '8': '0110111',
      '9': '0001011'}
TC = int(input())
for tc in range(1, TC + 1):
    n, m = map(int, input().split())
    brd = [input() for _ in range(n)]
    sy = 0
    for y in range(n):
        if '1' in brd[y]:
            sy = y
            break
    cnt = 0
    result = []
    idx = m - 1
    while cnt < 8:
        if brd[sy][idx] == '1':
            cnt += 1
            for p, v in pw.items():
                if v == brd[sy][idx - 6: idx + 1]:
                    result.append(int(p))
            idx -= 7
        else:
            idx -= 1
    result.reverse()

    if ((result[0] + result[2] + result[4] + result[6]) * 3 + result[1] + result[3] + result[5] + result[7]) % 10:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {sum(result)}')
