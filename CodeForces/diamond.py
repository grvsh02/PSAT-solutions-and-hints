m = int(input("please enter the no. of rows for traingle"))
n = m
k = 1
for i in range(n):

    j = n
    for i in range (j):
        print(" ",end="")
    
    for i in range (k):
        print("*",end="")
    
    print("")
    n = n - 1
    k = k + 2

n = m 
j = 1

for l in range(n,0,-1):
    
    
    for i in range (l+1):
        print(" ",end="")
    
    for i in range (l*2-1):
        print("*",end="")
    
    print("")
    n = n - 1
    