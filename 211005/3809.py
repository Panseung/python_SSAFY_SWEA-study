T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = ''
    while len(S) != N:
        S += input()
        S = S.replace(' ', '')

    case = []   #3, 0, 1, 30, 01, 301
    scope = 1
    while scope <= N:
        for i in range(len(S) + 1 - scope):
            case.append(int(S[i:i + scope]))
        scope += 1
    case = list(set(case))
    case.sort()

    if case[0] != 0:
        print(f'#{tc} 0')
    elif case[1] != 1:
        print(f'#{tc} 1')
    else:
        for i in range(len(case)):
            if case[i+1] - case[i] != 1:
                print(f'#{tc} {case[i]+1}')
                break