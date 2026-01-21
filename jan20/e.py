# args — dynamic list
def to_string(*args, sep=' ', end='\n'):
    result = ''
    # enumerate - (index, elem)
    for i, item in enumerate(args):
        if i > 0:
            result += sep
        result += str(item)
    result += end
    return result
