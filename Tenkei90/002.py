def generate01(n):
    return [format(i, f'0{n}b') for i in range(2**n)]

n = int(input())

zo = generate01(n)

for i in zo:
    judge = True
    left = 0
    right = 0
    for j in i:
        if j=='0':
            left += 1
        else:
            right += 1
            if right > left:
                judge = False
    if judge and left==right:
        ans = ""
        for j in i:
            if j=='0':
                ans += "("
            else:
                ans += ")"
        print(ans)
    