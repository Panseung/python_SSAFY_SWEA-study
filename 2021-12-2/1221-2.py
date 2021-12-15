# 1221. [S/W 문제해결 기본] 5일차 - GNS
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14jJh6ACYCFAYD

num_dic = {'ZRO': 0,
           'ONE': 1,
           'TWO': 2,
           'THR': 3,
           'FOR': 4,
           'FIV': 5,
           'SIX': 6,
           'SVN': 7,
           'EGT': 8,
           'NIN': 9}

reverse_num_dic = {0: 'ZRO',
                   1: 'ONE',
                   2: 'TWO',
                   3: 'THR',
                   4: 'FOR',
                   5: 'FIV',
                   6: 'SIX',
                   7: 'SVN',
                   8: 'EGT',
                   9: 'NIN'}

TC = int(input())
for tc in range(1, TC + 1):
    test_num, length = input().split()
    num_lst = list(input().split())
    tmp_lst = list()
    for alpha in num_lst:
        tmp_lst.append(num_dic[alpha])
    tmp_lst.sort()
    result = list()
    for num in tmp_lst:
        result.append(reverse_num_dic[num])

    print(test_num)
    print(*result)
