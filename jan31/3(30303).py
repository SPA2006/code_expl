for i in range(1048575, 0, -1):
    s = hex(i // 2)[2:]
    if i % 4 != 0:
        s = 'f' + s + 'a0'
    else:
        s = '15' + s + 'c'
    if int(s, 16) < 1048576:
        print(i)
        break
