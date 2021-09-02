TC = int(input())
for tc in range(1, TC+1):
    p, q = map(float, input().split())
    s1 = (1-p) * q
    s2 = p*(1-q)*q
    if s2 > s1:
        result = 'YES'
    else:
        result = 'NO'
    print(f'#{tc} {result}')