def secret_replace(text, **rules):
    for key, values in rules.items():
        i = 0
        result = []
        n = len(values)
        for ch in text:
            if ch == key:
                result.append(values[i % n])
                i += 1
            else:
                result.append(ch)
        text = ''.join(result)
    return text
