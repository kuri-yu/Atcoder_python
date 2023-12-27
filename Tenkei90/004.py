h,w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

sumh = [sum(a[i]) for i in range(h)]
sumw = []
for i in range(w):
    s = 0
    for j in range(h):
        s += a[j][i]
    sumw.append(s)

b = [[] for i in range(h)]

for i in range(h):
    for j in range(w):
        b[i].append(sumh[i] + sumw[j] - a[i][j])
    print(' '.join(map(str, b[i])))