n = int(input())

for i in range(n):
    m = int(input())
    l = list(map(int,input().split()))

    if l[0] != l[1]:

        if l[1] == l[-1]:
            print(0)
            continue

    for j in range (1,len(l)):

        if l[j - 1] != l[j]:
            print(j)
            break
