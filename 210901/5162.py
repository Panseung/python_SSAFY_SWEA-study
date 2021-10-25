# 5162. 두가지 빵의 딜레마
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWTaTDua3OoDFAVT


TC = int(input())
for tc in range(1, TC + 1):
    A, B, C = map(int, input().split())  # 현미가격, 단호박가격, 현재 자금
    bread = A
    if A > B:
        bread = B
    result = C // bread
    print(f'#{tc} {result}')
