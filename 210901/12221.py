TC = int(input())
for tc in range(1, TC+1):
    A, B = map(int, input().split())
    if A >= 10 or B >= 10:
        result = -1
    else:
        result = A*B
    print(f'#{tc} {result}')