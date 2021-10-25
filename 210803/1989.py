# 1989. 초심자의 회문 검사
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PyTLqAf4DFAUq


cnt = int(input())
for i in range(cnt):
    word = input()
    result = 0
    for j in range(len(word) // 2):
        if word[j] != word[-j - 1]:
            result += 0
        else:
            result += 1
    if result == 0:
        print(f'#{i + 1} 0')
    else:
        print(f'#{i + 1} 1')
