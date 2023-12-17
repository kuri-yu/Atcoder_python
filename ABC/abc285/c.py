s = input()
nums = len(s)

ans = 0

for i in range(nums-1, -1, -1):
    ans += 26 ** i * (ord(s[(nums-1)-i])-64)

print(ans)