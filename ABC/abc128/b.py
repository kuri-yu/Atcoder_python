n = int(input())
a = []
for i in range(n):
    s, p = map(str, input().split())
    p = int(p)
    a.append([s, -p, i+1])

a.sort()
for a_ in a:
    print(a_[2])