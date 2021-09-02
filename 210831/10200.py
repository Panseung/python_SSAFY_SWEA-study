TC = int(input())
for tc in range(1, TC+1):
    N, A, B = map(int, input().split())
    minV = A + B - N
    if minV < 0:
        minV = 0
    maxV = A
    if A > B:
        maxV = B
    print(f'#{tc} {maxV} {minV}')





# TC = int(input())
# for tc in range(1, TC+1):
#     N, A, B = map(int, input().split())
#     minV = A + B - N
#     if minV < 0:
#         minV = 0
#     maxV = min([A, B])
#     print(f'#{tc} {maxV} {minV}')