n = int(input())
marks = []
for i in range(n):
    a,b,c,d = [int(x) for x in input().split()]
    marks.append(a+b+c+d)
rank = marks[0]
marks.sort(reverse=True)

print(marks.index(rank) + 1)

