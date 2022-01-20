n = int(input())
s = input()
d = {}

for i in range(n-1):

    gram = s[i] + s[i+1]
    d.setdefault(gram,0)
    d[gram] += 1
    
print(max(d, key=d.get))
