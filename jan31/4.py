mx = 0
for n in range(1, 300):
    f = ''
    # четверичная запись числа
    while n > 0:
        f = str(n % 4) + f
        n //= 4
    f += f[-1]
    b = bin(int(f, 4))[2:]
    b += b[-1]
    r = int(b, 2)
    if r < 280:
        print(r)
        mx = max(r, mx)

print()
print()
print(mx)
