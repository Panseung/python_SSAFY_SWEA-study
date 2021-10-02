TC = int(input())
for tc in range(1, TC+1):
    A, B = map(int, input().split())
    rate = A/B
    result = rate * rate
    print(f'#{tc} {int(result)}')