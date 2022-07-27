# 4466. 최대 성적표 만들기
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWOUfCJ6qVMDFAWg&categoryId=AWOUfCJ6qVMDFAWg&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4

TC = int(input())
for tc in range(1, TC + 1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    print(f'#{tc} {sum(scores[:k])}')
