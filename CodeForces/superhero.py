s1 = input()
s2 = input()

vowel =["a","e","i","o","u"]

if len(s1) != len(s2):
    print("No")
else :
    for i in range(len(s1)):
        if (s1[i] in vowel and s2[i] not in vowel) or (s1[i] not in vowel and s2[i] in vowel):
            print("No")
            break
    else:
        print("Yes")
