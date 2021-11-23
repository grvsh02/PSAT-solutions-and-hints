n = int(input())

for i in range(n):

    a,b,c = [int(x) for x in input().split()]
    max_no =  max(a, b, c)
    arr = []
    
    if max(c, b) < a:       

        print(0,end= " ")

    else:

        print(max_no - a + 1, end= " ")

    if max(a, c) < b:

        print(0,end= " ")

    else:

        print(max_no - b + 1, end= " ")

    if max(b, a) < c:

        print(0,end= " ")

    else:
        
        print(max_no - c + 1)