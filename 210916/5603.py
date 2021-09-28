TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(int(input()))
    avg = sum(lst) // N
    result = 0
    for i in range(N):
        result += abs(avg - lst[i])
    print(f'#{tc} {int(result * 0.5)}')
