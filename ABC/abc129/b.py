n = int(input())
w = list(map(int, input().split()))

mins = sum(w)

for i in range(1,n):
    mins = min(mins, abs(sum(w[0:i]) - sum(w[i:])))

print(mins)