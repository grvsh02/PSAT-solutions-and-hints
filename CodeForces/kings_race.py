n = int(input())
x,y = map(int,input().split())

white = (x-1) + (y-1)
black = (n-x) + (n-y)

if white > black:
    print("Black")
else:
    print("White")