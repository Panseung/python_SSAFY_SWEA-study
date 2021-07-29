
cnt = int(input())      #시행횟수 첫줄 입력

for i in range(cnt):
    k = int(input())
    n = 1
    a = k
    lst = []
    while len(lst) != 10 :
        for j in range(len(str(a))):
            if str(a)[j] not in lst:
                lst.append(str(a)[j])
        n += 1
        a = k * n

        
    print(k*(n-1))
