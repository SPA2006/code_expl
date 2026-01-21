def find_mountains(heights):
    mountains = []
    n = len(heights)
    for i in range(n):
        if i > 0:
            left = heights[i - 1]
        else:
            left = float('+inf')
        if i < n - 1:
            right = heights[i + 1]
        else:
            right = float('+inf')
        
        if heights[i] > left and heights[i] > right:
            mountains.append(i + 1)
    return tuple(mountains)
