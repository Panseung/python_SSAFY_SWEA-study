# 1759. 암호 만들기
# Level Gold 5
# link : https://www.acmicpc.net/problem/1759


def solve(n, word, length, cnt1, cnt2):  # n:인덱스 word:암호 length:암호길이 cnt1:모음수 cnt2:자음수
    if n == C:  # 알파벳 모두 확인했으면 리턴
        if length == L and cnt1 >= 1 and cnt2 >= 2:
            case.append(word)
        return
    else:
        solve(n + 1, word, length, cnt1, cnt2)  # 현재 인덱스 글자 안넣고 재귀 들어가기
        if s[n] in vowel_lst:  # 넣을 글자가 모음일 때
            solve(n + 1, word + s[n], length + 1, cnt1 + 1, cnt2)
        else:  # 넣을 글자가 자음일 때
            solve(n + 1, word + s[n], length + 1, cnt1, cnt2 + 1)


L, C = map(int, input().split())  # 암호 길이, 알파벳 숫자
s = list(input().split())
s.sort()
vowel_lst = ['a', 'e', 'i', 'o', 'u']
case = []
solve(0, '', 0, 0, 0)
case.sort()
for i in case:
    print(i)



