n = int(input())
s = input()

for i in range(1,n):
    k = 0
    while i + k < n:
        if s[k] == s[i+k]:
            print(k)
            break
        elif i+k == n-1:
            print(k+1)
            break
        k += 1