# 4751. 다솔이의 다이아몬드 장식
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWSNw5jKzwMDFAUr&categoryId=AWSNw5jKzwMDFAUr&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2

TC = int(input())
for tc in range(1, TC + 1):
    S = input()
    first = '.'
    sec = '.'
    thr = '#'
    for i in range(len(S)):
        first += '.#..'
        sec += '#.#.'
        thr += f'.{S[i]}.#'
    print(first)
    print(sec)
    print(thr)
    print(sec)
    print(first)

