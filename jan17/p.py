# 1. Пытаешься сравнить элемент, как если бы он был списком
# 2. Если операция не доступна для типа, то выполняем
#    ветку TypeError

def is_palindrome(x):
    try:
        return x == x[::-1]
    except TypeError:
        s = str(x)
        return s == s[::-1]
