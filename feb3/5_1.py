# O(M^N)
# _   _ _   _
# x1 x2 x3 x4
# _ _ _ _

a = "САМОРЗВИТЕ"
count = 0
for x1 in a:
  for x2 in a:
    for x3 in a:
      for x4 in a:
        s = x1 + x2 + x3 + x4
        if len(s) == len(set(s)):
          count += 1

print(count)
