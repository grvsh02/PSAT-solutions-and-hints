n = input()
count = 1
flag = "2"
for i in n:
    if i == flag :
        count = count + 1
    else :
        count = 1
        flag = i
    if count == 7:
        print("YES")
        break
else:
    print("NO")
