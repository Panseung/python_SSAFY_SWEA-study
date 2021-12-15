TC = int(input())
for tc in range(1, TC+1):
    line = input()

    # 레이저 갯수 및 시작위치 구하기
    pos = 0
    lst_l = [] #레이저를 'O'로 바꾼 리스트
    while pos < len(line):
        if line[pos:pos+2] == '()':
            lst_l.append('O')
            pos += 2
        else:
            lst_l.append(line[pos])
            pos += 1
    stack = []
    cnt = 0
    for i in lst_l:
        if i == '(':
            stack.append(i)
            cnt += 1
        if i == ')':
            stack.pop(-1)
        if i == 'O':
            cnt += len(stack)
    print(f'#{tc} {cnt}')
