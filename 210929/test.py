ans = []
my_ans = []
for i in range(1347):
    ans.append(input())
for i in range(1347):
    my_ans.append(input())

for i in range(1347):
    if ans[i] != my_ans[i]:
        print(i)
print(len(ans))
