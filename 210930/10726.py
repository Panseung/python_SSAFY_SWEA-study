TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())

    S = ''
    while M >= 1:
        if M % 2 == 1:
            S += '1'
        else:
            S += '0'
        M = M // 2

    bit_1 = 0
    for i in range(N):
        if len(S) >= N and S[i] == '1':
            bit_1 += 1

    if bit_1 == N:
        result = 'ON'
    else:
        result = 'OFF'

    print(f'#{tc} {result}')

