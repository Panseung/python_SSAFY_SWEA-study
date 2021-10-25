# 2007. 패턴 마디의 길이
# Level D2
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P1kNKAl8DFAUq


cnt = int(input())
for i in range(cnt):
    word = input()
    p_word = ""
    for j in range(1, 16):
        p_word += word[j - 1]
        if word[0:j] == word[j:2 * j]:
            break
    print(f'#{i + 1} {len(p_word)}')
