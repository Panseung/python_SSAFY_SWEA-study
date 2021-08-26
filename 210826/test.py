n = int(input()) # 스위치 개수
states = list(map(int, input().split()))
# 남 : 1 , 여 : 2
nums = int(input()) # 학생 수
lst = []
for i in range(nums):
    st, k = map(int, input().split())
    lst.append(st)
    lst.append(k)

for i in range(nums): # 0 1
    if lst[2*i] == 1:
        a = lst[2*i+1]  # 3
        for j in range(a, len(states)+1, a): # 0 1 2 3 4 5 6 7
            if states[j-1] == 1:
                states[j-1] = 0
            elif states[j-1] == 0:
                states[j-1] = 1
    elif lst[2*i] == 2:
        a = lst[2*i+1] # 3
        idx = []
        states[a-1] = (states[a-1] + 1) % 2
        for z in range(len(states)//2): # 0 1 2 3
            if 0 <= a-z-2 and n > a+z:    ## z 가 2 일때 a-z-2 가 -1 이 되어서 0 <= -1 조건문에 들어가면 안되는데 왜 들어가는거졍?
                if states[a-2-z] == states[a+z]:
                    states[a-2-z] = (states[a-2-z] + 1) % 2
                    states[a + z] = (states[a+z] + 1) % 2
                else:
                    break

line = []
for i in range(0, len(states), 20):
    line.append(states[i:i+20])
for l in line:
    print(*l)
