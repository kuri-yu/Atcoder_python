# 動的計画法

mod = 10**9+7
n,m = map(int, input().split())
A_ = [int(input()) for _ in range(m)]
A = [0] * (n+3)
for a in A_:
    A[a] = 1
dp = [0] * (n+3)
dp[0] = 1
for i in range(1, n+1):
    if A[i-1] == 0:
        dp[i] += dp[i-1]
    if A[i-2] == 0:
        dp[i] += dp[i-2]
    dp[i] %= mod
print(dp[n])
