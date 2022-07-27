# 13229. 일요일
# Level D3
# Link : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX0SaDW6L2oDFASs&categoryId=AX0SaDW6L2oDFASs&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=3

weeks = {1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT', 7: 'SUN'}

TC = int(input())
for tc in range(1, TC + 1):
    s = input()
    for val, week in weeks.items():
        if week == s:
            result = 7 - val
            if result == 0:
                result = 7
            print(f'#{tc} {result}')
            break
