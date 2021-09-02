TC = int(input())
for tc in range(1, TC+1):
    s = input()
    result = ''
    vowel = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i not in vowel:
            result += i
    print(f'#{tc} {result}')
