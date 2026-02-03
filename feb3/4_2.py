from itertools import permutations

count = 0
for x in permutations("ПРАВНУК"):
  s = "".join(x)
  if s[0] == "П" and s[-1] == "Р":
    count += 1

print(count)
