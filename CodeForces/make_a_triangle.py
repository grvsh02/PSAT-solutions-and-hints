x,y,z = [int(x) for x in input().split()]

if x >= (y+z):
    ans = x - (y+z)+1
elif  y >= (z+x):
    ans = y - (z+x)+1
elif z >= (x+y):
    ans = z - (x+y)+1
else :
    ans = 0

print(ans)
