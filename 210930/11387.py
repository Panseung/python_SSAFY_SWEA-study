TC = int(input())
for tc in range(1, TC+1):
    D, L, N = map(int, input().split()) # 기본데미지, 증뎀, 공격횟수
    damage = 0
    for n in range(N):
        damage += D * (1 + n*L*0.01)
    print(f'#{tc} {int(damage)}')
