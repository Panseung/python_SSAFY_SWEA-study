lst = [True] * (1000001)  # 에라토스테네스의 체를 각 케이스마다 하지 않고 한 번 돌려서 사용하여 시간단축효과 기대
lst[0] = False
lst[1] = False
prime_lst = []  ##
pos = 2
while pos <= 1000001:
    prime_lst.append(pos)  ##
    for i in range(pos*2, 1000001, pos):
        lst[i] = False

    for i in range(pos+1, 1000001):
        if lst[i]:
            next_pos = i
            break
    if next_pos == pos:
        break
    else:
        pos = next_pos


T = int(input())
for tc in range(1, T+1):
    D, A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B+1):  # A와 B 사이에 있는 범위만 반복문 실행하기
        if str(D) in str(i) and lst[i]:  # 각 숫자를 str타입으로 바꾸어 숫자에 D가 들어가있는지 확인하고 소수인지 확인한 후
            cnt += 1  # 소수가 맞으면 cnt +1 해주기
    print(f'#{tc} {cnt}')

