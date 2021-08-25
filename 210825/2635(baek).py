def connecting(lst):
    global N
    M = N-1
    maxV = 0
    result = []
    while M >= 0:
        lst.append(M)
        while lst[-2] > lst[-1]:
            lst.append(lst[-2] - lst[-1])
        if len(lst) > maxV:
            maxV = len(lst)
            result = lst[:]
        M -= 1
        lst = [N]
    return [maxV, result]


N = int(input())
lst = [N]
print(connecting(lst)[0])
print(*connecting(lst)[1])