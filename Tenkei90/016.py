n = int(input())
a = list(map(int, input().split()))
a.sort()

maisu = 10000

for i in range(n//a[2]+1):
    for j in range(n//a[1]+1):
        if n - i*a[2] - a[1]*j >= 0 and (n - i*a[2] - a[1]*j)%a[0]==0:
            maisu = min(maisu, i+j+(n - i*a[2] - a[1]*j)//a[0])

print(maisu)
