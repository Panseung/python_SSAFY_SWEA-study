TC = int(input())
for tc in range(1, TC+1):
    S = input()
    lst = []
    result = [13, 13, 13, 13]
    test = True
    for i in range(0,len(S),3):
        pattern = S[i]
        card = S[i] + S[i+1] + S[i+2]
        if pattern == 'S':
            result[0] -= 1
        elif pattern == 'D':
            result[1] -= 1
        elif pattern == 'H':
            result[2] -= 1
        else:
            result[3] -= 1
        if card in lst:
            test = False
        lst.append(card)

    if test:
        print(f'#{tc}', end=' ')
        print(*result)
    else:
        print(f'#{tc} ERROR')

