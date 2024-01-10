n = int(input())
while True:
  if (n // 100) * ((n % 100) // 10) == n % 10:
    exit(print(n))
  n += 1