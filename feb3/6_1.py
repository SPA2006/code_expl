a = "НРДО" # надо вот так
# a = "ДРОН" (вот так вот не надо)))
count = 0

for x1 in a:
  for x2 in a:
    for x3 in a:
      for x4 in a:
        s = x1 + x2 + x3 + x4
        count += 1
        if s == "ДРОН":
          print(count)
          break
