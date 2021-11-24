n = int(input())
s = input()
ans = ""
i = 0
n = 1
while i < len(s) :
    ans = ans + s[i]
    i = i + n
    n = n + 1
print(ans)
