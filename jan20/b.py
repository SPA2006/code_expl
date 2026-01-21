def make_matrix(size, value=0):
    mat = []
    print(str(type(size)))
    if str(type(size))[-3] == 't':
        # число
        for x in range(size):
            mat.append([value] * size)
    else:
        # tuple (кортеж)
        for x in range(size[1]):
            mat.append([value] * size[0])
    return mat
