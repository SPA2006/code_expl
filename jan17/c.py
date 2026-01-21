def number_length(n):
    n = abs(n)
    if n == 0:
        return 1
    length = 0
    while n > 0:
        n //= 10
        length += 1
    return length
