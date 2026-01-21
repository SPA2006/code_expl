def find_mountains(data):
    rows = len(data)
    cols = len(data[0])
    mnts = []

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            current = data[i][j]
            is_mnt = True

            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    if data[i + di][j + dj] >= current:
                        is_mnt = False
                        break
                    if not is_mnt:
                        break
            if is_mnt:
                mnts.append((i + 1, j + 1))

    return tuple(mnts)
