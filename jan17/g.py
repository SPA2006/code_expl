def max2D(matrix):
    max_val = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > max_val:
                max_val = elem
    return max_val
