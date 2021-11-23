s = input()
ans = s.count("a")
ans = ans * 2 -1
if ans > len(s):
    print(len(s))
else : 
    print(ans)