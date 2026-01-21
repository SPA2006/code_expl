def split_numbers(text):
    numbers = text.split()
    return tuple(int(num) for num in numbers)
