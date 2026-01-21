def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# gcd(7, 15) # actual parameters (фактические параметры)
# gcd(3, 6) # the answer: 3
