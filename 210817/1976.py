TC = int(input())
for tc in range(1, TC+1):
    h1, m1, h2, m2 = map(int, input().split())
    result = (h1+h2)*60 + m1 + m2
    h = (result // 60) % 12
    if h == 0:
        h = 12
    m = result % 60
    print(f'#{tc} {h} {m}')