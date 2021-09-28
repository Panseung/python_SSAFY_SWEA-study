import itertools
TC = int(input())
for tc in range(1, TC+1):
    lst1 = list(map(int, input().split()))
    lst2 = lst1[:]
    lst3 = lst1[:]
    pair = list(itertools.product(lst1, lst2, lst3))
    result = []
    for i in range(len(pair)):
        if len(set(pair[i])) == 3 and sum(pair[i]) not in result:
            result.append (sum(pair[i]))
    result.sort(reverse=True)
    print(f'#{tc} {result[4]}')
