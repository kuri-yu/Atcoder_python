n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

num = 0

for i in range(n):
    num += abs(a[i]-b[i])

print('Yes' if k>=num and (k-num)%2==0 else 'No')