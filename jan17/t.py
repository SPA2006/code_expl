def roman(a, b):
    # преобразует арабскую запись к римской
    def to_roman(n):
        values = [
            (1000, 'M'), (900, 'CM'), (500, 'D'),
            (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
            (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'),
            (4, 'IV'), (1, 'I')
        ]
        result = []
        
        for val, sym in values:
            while n >= val:
                # записали
                result.append(sym)
                n -= val
        return ''.join(result)

    s = a + b
    ra = to_roman(a)
    rb = to_roman(b)
    rs = to_roman(s)

    return f'{ra} + {rb} = {rs}'
