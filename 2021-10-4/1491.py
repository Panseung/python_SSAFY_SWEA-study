T = int(input())
for tc in range(1, T + 1):
    N, A, B = map(int, input().split())



    result = 10000**3
    for n in range(1, N + 1):
        for i in range(1, n+1):
            if n * i > N:
                break
            if result > A*abs(n-i) + B*(N - n*i):
                result = A*abs(n-i) + B*(N - n*i)
    print(f'#{tc} {result}')
