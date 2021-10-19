T = int(input())
for tc in range(1, T+1):
    S = input()
    length = (len(S)-1) // 2 + 1                                # 입력문자열 S의 정 가운데 글자까지의 길이 + 1
    pattern = True                                              # 입력문자열 S를 앞에서부터 검사하여 하나라도 조건에 맞지 않으면 False로 바뀜
    for i in range(length):
        if S[i] == S[-i-1] or S[i] == '?' or S[-1-i] == '?':    # 맨 앞에서부터 대칭되는 글자가 같거나 둘 중 하나라도 '?'면 pattern은 True
            continue
        else:
            pattern = False
    if pattern:
        print(f'#{tc} Exist')
    else:
        print(f'#{tc} Not exist')