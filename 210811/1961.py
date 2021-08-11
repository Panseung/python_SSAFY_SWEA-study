CT = int(input())
for w in range(1, CT+1):
    N = int(input())
    lst = []
    lst1 = []
    lst2 = []
    lst3 = []
    for q in range(N):
        lst.append(list(map(str, input().split())))

    big_pot = [] #1
    for y in range(N):
        pot = ''
        for x in range(N-1, -1, -1):
            pot += (lst[x][y])
        big_pot.append(pot)
    lst1.append(big_pot)
    
    big_pot = [] #2
    for y in range(N-1, -1, -1):
        pot = ''
        for x in range(N-1, -1, -1):
            pot += (lst[y][x])
        big_pot.append(pot)
    lst2.append(big_pot)

    big_pot = [] #3
    for y in range(N-1, -1, -1):
        pot = ''
        for x in range(N):
            pot += (lst[x][y])
        big_pot.append(pot)
    lst3.append(big_pot)   
   
    '''print(lst1)
    print(lst2)
    print(lst3)'''

    print(f'#{w}')
    for i in range(N):
        print(lst1[0][i], end=' ')
        print(lst2[0][i], end=' ')
        print(lst3[0][i])
