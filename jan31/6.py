for i in range(1000, 10000):
    s = str(i)
    x1 = int(s[0]) + int(s[1])
    x2 = int(s[2]) + int(s[3])

    if str(min(x1, x2)) + str(max(x1, x2)) == '1718':
        print(i)
        break
