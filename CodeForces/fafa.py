n = int(input())
ans = 0
 
for i in range(1, int(n/2) + 1):
    if (n - i) % i == 0:
        ans = ans + 1
 
print(ans)