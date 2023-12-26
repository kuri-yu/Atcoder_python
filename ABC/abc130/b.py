n,x = map(int, input().split())
l = list(map(int, input().split()))
ans = 1
z = 0
for i in range(n):
    z += l[i]
    if z <= x:
        ans += 1

print(ans)