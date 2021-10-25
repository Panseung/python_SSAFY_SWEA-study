# 1288. 새로운 불면증 치료법
# Level D2
# link : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18_yw6I9MCFAZN

cnt = int(input())  # 시행횟수 첫줄 입력

for i in range(cnt):
    k = int(input())
    a = k
    n = 0
    lst = []
    while len(lst) != 10:
        for j in range(len(str(a))):
            if str(a)[j] not in lst:
                lst.append(str(a)[j])
        n += 1
        a += k

    print(f'#{cnt} {n}')
