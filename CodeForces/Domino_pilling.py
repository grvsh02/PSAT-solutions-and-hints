x,y = [int(x) for x in input().split()]
if (x*y)%2 == 0:
    print(int((x*y)/2))
else:
    print(int((x*y-1)/2))