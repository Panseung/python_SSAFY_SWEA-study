# 5356. 의석이의 세로로 말해요
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVWgkP6sQ0DFAUO

TC = int(input())
for tc in range(1, TC + 1):
    words = list()
    longest = 0
    for _ in range(5):
        word = input()
        words.append(word)
        if len(word) > longest:
            longest = len(word)

    result = ''
    for i in range(longest):
        for word in words:
            if len(word) > i:
                result += word[i]

    print(f'#{tc} {result}')
