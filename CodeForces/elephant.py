x = int(input())
y = x
ans = 0
steps = [5,4,3,2,1]
for i in steps:
    y = x
    x = x % i
    ans = ans + int(y/i)

print(ans)