s = input()
upper = 0
lower = 0
for i in s:
    if i.isupper():
        upper = upper + 1
    else:
        lower = lower + 1
if upper > lower:
    s = s.upper()
else:
    s = s.lower()
print(s)