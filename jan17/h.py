def fragments(numbers):
    # if list is empty
    if not numbers:
        return []
    
    # create a list of lists
    result = []
    cur_frag = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            cur_frag.append(numbers[i])
        else:
            result.append(cur_frag)
            cur_frag = [numbers[i]]

    result.append(cur_frag)
    return result

