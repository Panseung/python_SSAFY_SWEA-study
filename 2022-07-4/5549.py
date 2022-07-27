# 5549. 홀수일까 짝수일까
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWWxpEDaAVoDFAW4&categoryId=AWWxpEDaAVoDFAW4&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=3

TC = int(input())
for tc in range(1, TC + 1):
    n = int(input())
    print(f'#{tc} ', end='')
    if n % 2:
        print('Odd')
    else:
        print('Even')
