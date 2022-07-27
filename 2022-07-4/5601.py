# 5601. [Professional] 쥬스 나누기
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWXGAylqcdYDFAUo&categoryId=AWXGAylqcdYDFAUo&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2


TC = int(input())
for tc in range(1, TC + 1):
   n = int(input())
   print(f'#{tc} ', end='')
   for i in range(n):
       res = '1/'
       res += str(n)
       print(res, end=' ')
   print()