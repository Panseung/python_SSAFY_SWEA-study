TC = int(input())
for tc in range(1, TC+1):
    lst = list(input().split())
    N = int(lst.pop(0))
    lst_B = []
    lst_O = []
    lst_order = []
    for i in range(0, N*2, 2):
        if lst[i] == 'B':
            lst_B.append(int(lst[i+1]))
            lst_order.append('B')
        else:
            lst_O.append(int(lst[i+1]))
            lst_order.append('O')
    cnt = 0
    pos_B, pos_O = 1, 1
    button = True
    while lst_B or lst_O:
        button = True                               # B O O B
        if lst_B:
            if pos_B == lst_B[0] and lst_order[0] == 'B':
                lst_B.pop(0)
                lst_order.pop(0)
                button = False
            elif pos_B > lst_B[0]:
                pos_B -= 1
            elif pos_B < lst_B[0]:
                pos_B += 1
        if lst_O:
            if pos_O == lst_O[0] and lst_order[0] == 'O' and button:
                lst_O.pop(0)
                lst_order.pop(0)
            elif pos_O > lst_O[0]:
                pos_O -= 1
            elif pos_O < lst_O[0]:
                pos_O += 1
        cnt += 1
    print(f'#{tc} {cnt}')