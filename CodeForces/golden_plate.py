x,y,z = [int(a) for a in input().split()]
paint = 0

for i in range(z):
    paint = paint + (2*(x+y) - 5 )
    x = x - 4
    y = y - 4
    if x < 3:   
        break
    if y < 3:
        break

print(paint) 