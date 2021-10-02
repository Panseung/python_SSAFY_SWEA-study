TC = int(input())
for tc in range(1, TC+1):
    D, A, B, F = map(int, input().split())  # 기차사이거리, A, B, 파리의 속력

    speed_F = F / 3600  # 파리의 초속
    speed = (A+B) / 3600    # 두 열차의 초속 합
    distance = D    # 두 열차 사이의 거리

    second = distance / speed
    fly_distance = speed_F * second

    result = round(fly_distance, 6)
    print(f'#{tc} {result}')



