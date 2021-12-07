n = int(input())

for i in range (n):
    visitors = int(input())
    l = list(map(int,input().split()))
    upvotes = 0
    for i in l :
        if i == 1 or i == 3:
            upvotes += 1
    print(upvotes)