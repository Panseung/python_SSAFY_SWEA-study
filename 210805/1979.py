cnt = int(input())
for i in range(cnt):
    M, N = map(int, input().split())
    lst = []
    for j in range(M):
        lst.append(list(map(str, input().split())))
    for j in range(M):
        ary = ""
        len_word = ""
        for k in range(M):
            ary += lst[j][k]
        for k in range(M-N):
            len_word += "0"
        print(ary)
        print(len_word)    