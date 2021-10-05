T = int(input())

for tc in range(1, T+1):
    N = int(input().strip())

    S = ''
    while len(S) != N:
        S += input()
        S = S.replace(' ', '')

    num = 0
    while True:
        if str(num) not in S:
            break
        num += 1

    print(f'#{tc} {num}')