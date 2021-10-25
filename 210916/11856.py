# 11856. 반반
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXjS1GXqZ8gDFATi


TC = int(input())
for tc in range(1, TC + 1):
    S = input()
    if len(set(S)) == 2:
        pot1 = []
        pot2 = []
        pot1.append(S[0])
        for i in range(1, 4):
            if pot1[0] == S[i]:
                pot1.append(S[i])
            else:
                pot2.append(S[i])
        if len(pot1) == len(pot2):
            print(f'#{tc} Yes')
        else:
            print(f'#{tc} No')
    else:
        print(f'#{tc} No')
