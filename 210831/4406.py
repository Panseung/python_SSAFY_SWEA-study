# 4406. 모음이 보이지 않는 사람
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcD_66pUEDFAV8


TC = int(input())
for tc in range(1, TC + 1):
    s = input()
    result = ''
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i not in vowel:
            result += i
    print(f'#{tc} {result}')
