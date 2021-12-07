n = int(input())

for i in range(n):
    keyboard = input()
    word = input()
    time = 0
    if len(word) == 1:
        print(0)
        continue
    for i in range(len(word)- 1):  
        time = time + abs(keyboard.index(word[i]) - keyboard.index(word[i+1]))
    print(time)
