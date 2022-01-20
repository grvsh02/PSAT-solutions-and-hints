n = int(input())
l = list(map(int,input().split()))

l1= []
i = 1
sum = 0
flag = 0
for j in range(n):
    if l[j] == 0:
        continue
    flag = 1
    sum = sum + l[j]
    if sum == 0:
        l1.append([i,j])
        print(l1)
        i = j + 1
if flag == 1:
    print("YES")
    l1.append([i, j+1])
    print(len(l1))
    for i, j in l1:
        print(i, j)
else:
    print("NO")