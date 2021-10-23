case = []


T = int(input())
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    Alice = A/B
    Bob = C/D
    result = 'DRAW'
    if Alice > Bob:
        result = 'ALICE'
    elif Bob > Alice:
        result = 'BOB'
    case.append(f'#{tc} {result}')
for i in case:
    print(i)
