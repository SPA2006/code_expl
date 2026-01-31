# isinstance checks does 
# all any
# \forall \exists
# lambda item: isinstance(item[1], list) and any(isinstance(x, int) and x % 2 == 0 for x in item[1])
lambda item: type(item[1]) is list and any(type(x) is int and x % 2 == 0 for x in item[1])

# isinstance(var, type)
# type(var) is type
