TC = int(input())
for tc in range(1, TC+1):
    T = input()
    lst = []
    for i in T:
        lst.append(i)
    for i in range(len(lst)-1):
        for j in range(1, len(lst)-i):
            if lst[i] == lst[i+j]:
                lst[i], lst[i+j] = '0', '0'
    lst.sort()
    result = ''
    for i in lst:
        if i != '0':
            result += i
    if result == '':
        result = 'Good'
    print(f'#{tc} {result}')
