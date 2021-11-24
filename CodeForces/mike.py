s = input()
flag = 0
for i in range(len(s)//2):
    
    if s[i] != s[- i - 1]:
        
        if flag == 0:
            flag = 1
        else:
            print("NO")
            break
else:
    print("YES")
