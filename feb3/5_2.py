from itertools import permutations

count = 0
for x in permutations("САМОРЗВИТЕ", r=4):
  s = "".join(x)
  count += 1

print(count)
