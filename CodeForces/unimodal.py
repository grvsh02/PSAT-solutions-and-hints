n = int(input())
l = list(map(int,input().split()))
level = 1
change_collector = 0

for i in range(n - 1):
    if l[i] < l[i+1]:
        if change_collector == 0 and level == 1:
            pass
        else : 
            print("NO in 1")
            break
    if l[i] == l[i + 1] : 
        if change_collector == 1 and level == 2:
            pass
        elif change_collector == 0:
            change_collector = 1
            level = 2
        elif level != 2 :
            print(change_collector,level)
            print("NO in 2")
            break
    if l [i] > l [i + 1]:
        print(l[i],"hello" , l[i+1])
        if change_collector == 2 and level == 3:
            pass
        elif change_collector == 1 or change_collector == 0:
            change_collector = 2
            level = 3
        elif level != 3:
            print(change_collector,level)
            print("NO in 3")
            break
else :
    print("YES")