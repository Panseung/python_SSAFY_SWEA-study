TC = int(input())
for tc in range(1, TC+1):
    lst = []
    for i in input():
        lst.append(i)
    for i in range(len(lst)):
        if lst[i] == 'b':
            lst[i] = 'd'
        elif lst[i] == 'd':
            lst[i] = 'b'
        elif lst[i] == 'p':
            lst[i] = 'q'
        elif lst[i] == 'q':
            lst[i] = 'p'
    s = ''
    for i in lst:
        s += i
    s = s[::-1]
    print(f'#{tc} {s}')