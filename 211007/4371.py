T = int(input())
for tc in range(1, T+1):
    N = int(input())
    day_lst = []
    for _ in range(N):
        day_lst.append(int(input()))

    differences = []  #  배 주기 들어가는 리스트 6
    pos = 1
    while pos < len(day_lst):
        difference = day_lst[pos] - 1  # 배 주기 6
        differences.append(difference)
        del_lst = []  # 없앨 날짜들 인덱스 담는 리스트
        for i in range(pos+1, len(day_lst)):
            if (day_lst[i]-1) % difference == 0:  # 날짜들이 배 주기 차이면 지울 인덱스 리스트에 담기
                del_lst.append(i)
        del_lst.sort(reverse=True)
        for i in del_lst:
            day_lst.pop(i)
        pos += 1

    print(f'#{tc} {len(differences)}')

# 1
# 7
# 10