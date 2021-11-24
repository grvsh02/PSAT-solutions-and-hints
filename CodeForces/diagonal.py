n = int(input())
s = input()
count = 0
i = 0
while i < n-1:
    if s[i] != s[i+1]:
        i = i + 2
        count = count + 1
    else :
        i = i + 1
print(n-count)
