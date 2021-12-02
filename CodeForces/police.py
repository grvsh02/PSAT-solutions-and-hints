n = int(input())
l = list(map(int,input().split()))
a = 0
count = 0
for i in l:
    a = a + i
    if a < 0:
        count = count + 1
        a = 0

print(count)