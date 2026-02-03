from itertools import product

count = 0
for i in product("НРДО", repeat=4):
  s = "".join(i)
  count += 1
  if s == "ДРОН":
    print(count)
