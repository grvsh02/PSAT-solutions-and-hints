n,k = [int(x) for x in input().split()]
count = 0
for i in range(n):
    a = int(input())
    remainder = a%10
    while a > 0:
        if remainder > k:
            break
        else:
            a = a//10
            remainder = a%10
    else:
        count = count + 1
print(count)
