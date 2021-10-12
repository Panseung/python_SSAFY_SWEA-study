T = int(input())
for tc in range(1, T+1):
    s = input()
    people = int(s[0])
    hire = 0
    pos = 1

    while pos < len(s):
        if int(s[pos]) != 0:
            if people >= pos:
                people += int(s[pos])
            else:
                hire += pos - people
                people += pos - people
                people += int(s[pos])
        pos += 1
    print(f'#{tc} {hire}')
