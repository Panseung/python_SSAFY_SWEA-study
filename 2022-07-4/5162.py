# 5162. 두가지 빵의 딜레마
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWTaTDua3OoDFAVT&categoryId=AWTaTDua3OoDFAVT&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4

TC = int(input())
for tc in range(1, TC + 1):
    a, b, c = map(int, input().split())
    print(f'#{tc} {c // min(a, b)}')
