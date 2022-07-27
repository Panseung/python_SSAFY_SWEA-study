# 5948. 새샘이의 7-3-5 게임
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWZ2IErKCwUDFAUQ&categoryId=AWZ2IErKCwUDFAUQ&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6

TC = int(input())
for tc in range(1, TC + 1):
    lst = list(map(int, input().split()))
    sum_lst = []
    for i in range(5):
        for j in range(i + 1, 6):
            for k in range(j + 1, 7):
                sum_lst.append(lst[i] + lst[j] + lst[k])
    sum_lst = list(set(sum_lst))
    sum_lst.sort(reverse=True)
    print(f'#{tc} {sum_lst[4]}')
