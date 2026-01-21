def take_small(money):
    result = []
    for value in money:
        if value < 100:
            result.append(value)
    return result
