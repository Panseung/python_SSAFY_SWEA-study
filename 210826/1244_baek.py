# 1244. 스위치 켜고 끄기
# 백준
# Link : https://www.acmicpc.net/problem/1244


def on_off(s, n):  # s = 성별, n = 스위치 숫자
    if s == 1:  # 남자
        for i in range(n - 1, len(status), n):
            status[i] = (status[i] + 1) % 2
    else:  # 여자
        status[n - 1] = (status[n - 1] + 1) % 2
        left = n - 2
        right = n
        if left >= 0 and right < len(status):
            while status[left] == status[right]:
                status[left] = (status[left] + 1) % 2
                status[right] = (status[right] + 1) % 2
                left -= 1
                right += 1
                if left < 0 or right >= len(status):
                    break
    return status


cnt = int(input())
status = list(map(int, input().split()))
N = int(input())
students = []
for _ in range(N):
    students += list(map(int, input().split()))
for i in range(0, len(students), 2):
    on_off(students[i], students[i + 1])
line = []
for l in range(0, len(status), 20):
    line.append(status[l:l + 20])
for l in line:
    print(*l)
