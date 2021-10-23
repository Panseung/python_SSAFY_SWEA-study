def solve(s1_pos, s2_pos, length):
    global result
    if s1_pos == len(S1) or s2_pos == len(S2):
        if length > result:
            result = length
        return
    else:
        a = len(S1) - s1_pos
        b = len(S2) - s2_pos
        if result - length < min(a, b):
            for i in range(s2_pos, len(S2)):
                if S1[s1_pos] == S2[i]:
                    solve(s1_pos+1, i+1, length +1)
            solve(s1_pos+1, s2_pos, length)





T = int(input())
for tc in range(1, T+1):
    S1_origin, S2_origin = input().split()

    S1 = ''
    S2 = ''
    for i in S1_origin:
        if i in S2_origin:
            S1 += i
    for i in S2_origin:
        if i in S1:
            S2 += i
    result = 0
    solve(0, 0, 0)
    print(f'#{tc} {result}')