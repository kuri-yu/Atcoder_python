def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a,b,c = map(int, input().split())
num = gcd(a, gcd(b,c))

print(a//num + b//num + c//num - 3)