TC = int(input())
for tc in range(1, TC+1):
    N = int(input())

    spiral_lst = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if N <= 10:
        result = spiral_lst[N-1]
    else:
        for i in range(10, N):
            spiral_lst.append(spiral_lst[i-1] + spiral_lst[i-5])
    result = spiral_lst[N-1]
    print(spiral_lst)
    print(f'#{tc} {result}')
