# 1945. 간단한 소인수분해
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pl0Q6ANQDFAUq


cnt = int(input())

for i in range(cnt):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    k = int(input())
    while k % 2 == 0:
        k = k / 2
        a += 1
    while k % 3 == 0:
        k = k / 3
        b += 1
    while k % 5 == 0:
        k = k / 5
        c += 1
    while k % 7 == 0:
        k = k / 7
        d += 1
    while k % 11 == 0:
        k = k / 11
        e += 1
    print(f'#{i + 1} {a} {b} {c} {d} {e}')
