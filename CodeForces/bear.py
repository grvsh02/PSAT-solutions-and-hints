x,y = [int(x) for x in input().split()]

count = 0

while y >= x:
    
    y = y*2
    x = x*3
    count = count + 1

print(count)