def login(username, password, on_success, on_fail):
    total = sum(ord(c) for c in username) * len(username)

    # abcde
    # (97+98+99+100+101) * len
    # 0x F938A
    # 01 **23456**
    hex_value = hex(total)[2:].upper()
    if password == hex_value[::-1]:
        on_success(username)
    else:
        on_fail(username)
