s = input()
vowel = ["a","e","i","o","u"]

for i in range (len(s)):
    if i != len(s) - 1:
        if s[i] not in vowel and s[i+1] not in vowel :
            if s[i] != "n":
                print("NO")
                break
    else :
        if s[i] != "n" and s[i] not in vowel:
            print("NO")
            break
else :
    print("YES")
