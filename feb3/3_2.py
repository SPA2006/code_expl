from itertools import product

count = 0
# *args, **kwargs
for x in product("РЕЦПТ", repeat = 6):
  _ = "".join(x)
  count += 1

print(count)
