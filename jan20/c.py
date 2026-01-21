# список произвольной длины
# dynamic list
# len(numbers) == 1; len(numbers) == 4
# (36, 48) => 12, (12, 156) => 12, (12, 100500) => 12
def gcd(*numbers):
    def gcd_two(a, b):
        while b:
            a, b = b, a % b
        return a
    
    result = numbers[0]
    if (len(numbers) > 1):
        for n in numbers[1:]:
            result = gcd_two(result, n)
    return result
