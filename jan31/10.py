for i in range(10000, 100000):
    s = str(i)
    x1 = int(s[0]) * int(s[0]) + int(s[2]) * int(s[2]) + int(s[4]) * int(s[4])
    x2 = int(s[1]) * int(s[1]) + int(s[3]) * int(s[3])
    if str(min(x1, x2)) + str(max(x1, x2)) == '36107':
        print(i)
        break
