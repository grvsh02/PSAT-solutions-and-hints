n = int(input())
ans = 0
for i in range(n):
    flag = 0

    x,y,z = [int(a) for a in input().split()]
    if x == 1:
        flag = flag + 1
    if y == 1:
        flag = flag + 1
    if z == 1:
        flag = flag + 1   
    if flag > 1:
        ans = ans + 1
print(ans)  