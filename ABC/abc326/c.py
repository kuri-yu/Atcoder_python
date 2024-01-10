from bisect import bisect_left as bsl
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
  ans = max(ans, bsl(a, a[i] + m) - i)
print(ans)