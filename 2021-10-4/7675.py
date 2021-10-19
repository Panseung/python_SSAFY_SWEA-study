T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(input().split())
    cnt_lst = [0] * N

    pos = 0
    for i in lst:
        low_cnt = 0  # 소문자 갯수
        if ord('A') <= ord(i[0]) <= ord('Z'):  # 첫글자 대문자면!

            if i[-1] == '!' or i[-1] == '?' or i[-1] == '.':  # 끝이 구두점이면!
                for j in range(1, len(i)-1):  # 두번째 글자부터 마지막 글자까지 소문자 갯수 세기
                    if ord('a') <= ord(i[j]) <= ord('z'):
                        low_cnt += 1
                if low_cnt == len(i)-2:  # 소문자 갯수랑 글자전체 갯수 -2랑 같으면
                    cnt_lst[pos] += 1  # 해당 문장의 인덱스에 +1 해주기

            else:  # 끝이 구두점이 아니면!
                for j in range(1, len(i)):
                    if ord('a') <= ord(i[j]) <= ord('z'):
                        low_cnt += 1
                if low_cnt == len(i) -1:
                    cnt_lst[pos] += 1
        if i[-1] == '!' or i[-1] == '?' or i[-1] == '.':  # 맨 마지막 단어가 구두점이면 인덱스 옮기기
            pos += 1

    print(f'#{tc}', end=' ')
    print(*cnt_lst)
