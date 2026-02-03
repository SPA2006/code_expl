# O(M^N)

a = "ПРАВНУК"
count = 0
for x1 in a:
  for x2 in a:
    for x3 in a:
      for x4 in a:
        for x5 in a:
          for x6 in a:
            for x7 in a:
              s = x1 + x2 + x3 + x4 + x5 + x6 + x7
              if len(s) == len(set(s)) and s[0] == "П" and s[-1] == "Р":
                count += 1

print(count)
