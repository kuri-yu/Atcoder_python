n = int(input())
one = []
two = []
sumone = 0
sumtwo = 0
s = [(0,0)]
for i in range(n):
    clas, score = map(int, input().split())
    if clas == 1:
        sumone += score
        one.append(sumone)
    else:
        sumtwo += score
        two.append(sumtwo)
    s.append((sumone, sumtwo))

q = int(input())
for i in range(q):
    l,r = map(int, input().split())
    print(s[r][0]-s[l-1][0], s[r][1]-s[l-1][1])
