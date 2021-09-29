lst = list(range(1000000))
lst_TF = [True] * 1000000
lst_TF[0] = False
lst_TF[1] = False
num = 2
while num <= 500000:
    print(num, end=' ')
    for i in range(num, len(lst), num):
        lst_TF[i] = False
    for i in range(num, len(lst)):
        if lst_TF[i] == True:
            next_num = i
            break
    if next_num == num:
        break
    else:
        num = next_num
