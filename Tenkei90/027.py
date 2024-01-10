n = int(input())
name = set()

for i in range(n):
    s = input()
    if not(s in name):
        name.add(s)
        print(i+1)