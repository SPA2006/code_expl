mx = 0

for i in range(1, 1000):
    f = ''
    n = i
    while n > 0:
        f = str(n % 7) + f
        n //= 7
    f = str(i % 5) + f + str(i % 3)
    r = int(f, 7)
    if len(str(r)) == 3:
        mx = max(mx, r)

print(mx)
